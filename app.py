import os
import cv2
import numpy as np
from base64 import b64decode
from flask import Flask, request, jsonify, make_response
from model.predict import predict

app = Flask(__name__)

def preflight_res():
    res_body = {"message": "Sending response to preflight request."}
    res = make_response(jsonify(res_body))
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return res

def create_res(res_body):
    res = make_response(jsonify(res_body))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.route('/classify_from_img', methods=['POST', 'OPTIONS'])
def classify_img():
    if request.method == 'OPTIONS':
        return preflight_res()

    req_body = request.get_json(force=True)
    img_data = req_body['image']
    img_arr = np.fromstring(b64decode(img_data), np.uint8)
    img_arr = cv2.imdecode(img_arr, cv2.COLOR_BGR2RGB)
    activation = predict(img_arr)

    if activation >= 0.5:
        animal = "cat"
    else:
        animal = "dog"

    res_body = {
        'animal': animal,
        'activation': str(activation)
    }
    return create_res(res_body)

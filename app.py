import os
from base64 import b64decode
from flask import Flask, request, jsonify, make_response
from model.predict import predict_path, predict_img

app = Flask(__name__)

def preflight_res():
    print("Preflight response!")
    res_body = {"message": "Sending response to preflight request."}
    res = make_response(jsonify(res_body))
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return res

def create_res(res_body):
    res = make_response(jsonify(res_body))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.route('/post_test', methods=['POST', 'OPTIONS'])
def post_test():
    if request.method == 'OPTIONS':
        return preflight_res()

    req = request.get_json()
    print(req)
    
    res_body = {"status": "Post successful"}
    return create_res(res_body)

@app.route('/classify_from_path', methods=['POST', 'OPTIONS'])
def classify_path():
    if request.method == 'OPTIONS':
        return preflight_res()
    
    req_body = request.get_json(force=True)
    path = req_body['path']

    activation = predict_path(path)
    if activation >= 0.5:
        animal = "cat"
    else:
        animal = "dog"

    res_body = {
        'activation': str(activation),
        'animal': animal
    }
    return create_res(res_body)


@app.route('/classify_from_img', methods=['POST', 'OPTIONS'])
def classify_img():
    if request.method == 'OPTIONS':
        return preflight_res()

    req_body = request.get_json(force=True)
    img_data = req_body['image'] 

    #decoding img and saving to temp file
    with open("temp.jpg", "wb") as fh:
        fh.write(b64decode(img_data))

    activation = predict_path("temp.jpg")
    if activation >= 0.5:
        animal = "cat"
    else:
        animal = "dog"

    #deleting temp.jpg
    os.remove("temp.jpg")

    res_body = ({
        'animal': animal,
        'activation': str(activation)
    })
    return create_res(res_body)

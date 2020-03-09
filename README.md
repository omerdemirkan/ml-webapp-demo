# ml-webapp-demo
Demonstrates how a full-stack web app can implement a neural net AI in its backend with a simple cat and dog image classifier.

Video: https://youtu.be/T8-JGrwK3_0

In the front end, the user selects a photo to classify. In script.js, this photo is read into the file_contents variable as a base64 encoded byte-string. When the user presses the classify button, the string encoding of the image is sent to the flask app backend (running from app.py) in an HTTP post request.

Because this request is cross-origin (the web page and back-end server are running on different ports), the browser automatically follows the CORS (cross-origin resource sharing protocol). This involves first sending an HTTP options request before the post request (this is called a preflight request), and checking the response the server sends to this request. If the response indicates that the request is allowed, the post request will be sent.

In the back-end (app.py), the /classify_from_img endpoint handles both options and post requests. When the preflight options request is sent, a proper response is sent back. Then, when the actual post request is sent, the base64 encoded byte-string representation of the image is decoding into the actual array representation of the image. 

The predict method from model/predict.py is then called with this array as its parameter. The method resizes and normalizes the image array, beforing feeding it to the pretrained VGG16 model. The method returns the model’s activation on this image.

App.py then packages this activation along with the corresponding label into a JSON object, which is sent back to the front-end as the response to the post request. Upon receiving this response, script.js then outputs the appropriate text to the web page.

*model/data.py was a script ran once to organize images in the dataset into different directories. model/model.py and model.generator.py were also scripts ran only once to train the model. script.js, app.py, and model/predict.py are the programs that are ran while the app is running.*


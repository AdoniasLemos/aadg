import os
from flask import Flask, request, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
import cv2
from keras.models import load_model
import numpy as np
import tensorflow as tf



global model
model = load_model('f2.h5')

global graph
graph = tf.get_default_graph()

def autoroi(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray_img, 130, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=5)

    contours, hierarchy = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    biggest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(biggest)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    roi = img[y:y+h, x:x+w]

    return roi


def prediction(photo):
    img = cv2.imread(photo)
    print("======================")
    print("===========PASSEI===========")
    print("======================")
    img = autoroi(img)

    print("======================")
    print("===========PASSEI DE NOVO===========")
    print("======================")
    img = cv2.resize(img, (256, 256))
    img = np.reshape(img, [1, 256, 256, 3])
    print("======================")
    print("===========PASSEI DE NOVO 2===========")
    print("======================")
    with graph.as_default():
        prob = model.predict(img)
    print("======================")
    print("===========PASSEI DE NOVO 3===========")
    print("======================")
    Class = prob.argmax(axis=-1)
    print("======================")
    print("===========PASSEI DE NOVO 4===========")
    print("======================")

    return(Class)


def run(photo):
    Class = prediction(photo)
    print (Class)


app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route("/")
def fileFrontPage():
    return render_template('upload.html')

@app.route("/uppload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            photo.save(os.path.join(app.root_path + '/static/result', photo.filename))
            run(os.path.join(app.root_path + '/static/result', photo.filename))
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    # BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    print(app.root_path + '/static/result')
    # print(os.path.join(BASE_DIR + 'static/result'))
    # app.debug = True
    app.run()     
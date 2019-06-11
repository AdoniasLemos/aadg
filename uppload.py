import os
from flask import Flask, request, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
import cv2
from keras.models import load_model
import numpy as np

model = load_model('f1.h5')

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
    img = autoroi(img)
    img = cv2.resize(img, (256, 256))
    img = np.reshape(img, [1, 256, 256, 3])

    prob = model.predict(img)
    Class = prob.argmax(axis=-1)

    return(Class)


def run(photo):
    Class = prediction(photo)
    # if (Class == 0):
    #     messagebox.showinfo('Prediction', 'You have been diagnosed with Glaucoma')
    # else:
    #     messagebox.showinfo('Prediction', 'Congratulations! You are Healthy')


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
            photo.save(os.path.join('static/result', photo.filename))
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    
    app.debug = True
    app.run()     
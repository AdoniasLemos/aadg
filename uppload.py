import os
from flask import Flask, request, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
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
            photo.save(os.path.join('/home/alessandra/UPP', photo.filename))
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    
    app.debug = True
    app.run()     
from crypt import methods
from urllib import response
from flask import *
app = Flask(__name__)
from Cartoonizer import Cartoonizer
import cv2
import os
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
CARTOON_IMAGE_FOLDER = 'static/cartoons/'
app.config['CARTOON_IMAGE_FOLDER'] = CARTOON_IMAGE_FOLDER


@app.route('/health')
def health():
    stat =  {
        "status": "OK"
    }
    return stat


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        #print(f)
        crt = Cartoonizer()
        res = crt.render(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        cv2.imwrite(os.path.join(app.config['CARTOON_IMAGE_FOLDER'], f.filename),res)
        original_image = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        cartoon_image = os.path.join(app.config['CARTOON_IMAGE_FOLDER'], f.filename)
    return render_template("success.html", name = f.filename,real = original_image,cartoon = cartoon_image)

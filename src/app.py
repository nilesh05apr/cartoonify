import os
import codecs
import numpy as np
from flask import *
from PIL import Image
from urllib import response
from AnimeGanv2 import model
from db import upload_cartoon_image, upload_real_image, get_real_image

app = Flask(__name__)


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
        real_image_id = upload_real_image(f,f.filename)
        img = Image.open(f.stream).convert("RGB")
        print(img.size)
        print(real_image_id)
        real_image = get_real_image(real_image_id)
        #print(real_image)

        # img.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        #f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        # out_celeba, out_facev1, out_facev2, out_paprika = model(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        out_celeba, out_facev1, out_facev2, out_paprika = model(img)
        
        # cartoon_image_id = upload_cartoon_image(out_celeba)
        # print(cartoon_image_id)

        out_celeba.save(os.path.join(app.config['CARTOON_IMAGE_FOLDER'], "out_celeba"+f.filename))
        out_facev1.save(os.path.join(app.config['CARTOON_IMAGE_FOLDER'], "out_facev1"+f.filename))
        out_facev2.save(os.path.join(app.config['CARTOON_IMAGE_FOLDER'], "out_facev2"+f.filename))
        out_paprika.save(os.path.join(app.config['CARTOON_IMAGE_FOLDER'], "out_paprika"+f.filename))

        original_image = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        celeba_image = os.path.join(app.config['CARTOON_IMAGE_FOLDER'], "out_celeba"+f.filename)
        facev1_image = os.path.join(app.config['CARTOON_IMAGE_FOLDER'], "out_celeba"+f.filename)
        facev2_image = os.path.join(app.config['CARTOON_IMAGE_FOLDER'], "out_celeba"+f.filename)
        paprika_image = os.path.join(app.config['CARTOON_IMAGE_FOLDER'], "out_celeba"+f.filename)
    
    return render_template("success.html", name = f.filename,
                            real = real_image,
                            celeba = celeba_image,
                            facev1=facev1_image,
                            facev2=facev2_image,
                            paprika=paprika_image)

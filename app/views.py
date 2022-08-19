from flask import *
from app import app
from PIL import Image
from os import environ as env
from .AnimeGanv2 import model
from .helpers.helper import byte_to_base64_str,image_to_byte_array




#app.config['UPLOAD_FOLDER'] = env['UPLOAD_FOLDER']
#app.config['MAX_CONTENT_LENGTH'] = int(env['MAX_CONTENT_LENGTH'])

#app.config['CARTOON_IMAGE_FOLDER'] = env['CARTOON_IMAGE_FOLDER']



@app.route('/health')
def health():
    stat =  {
        "status": "OK"
    }
    return stat


@app.route('/')
def home():
    return render_template("upload.html")


@app.route('/upload')
def upload():
    return render_template("upload.html")


@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
     
        f = request.files['file']
        img = Image.open(f.stream).convert("RGB")
     
        real_image_byte = image_to_byte_array(img)
        real_image = byte_to_base64_str(real_image_byte)

        out_celeba, out_facev1, out_facev2, out_paprika = model(img)

        out_celeba_byte = image_to_byte_array(out_celeba)
        out_celeba_img = byte_to_base64_str(out_celeba_byte)


        out_facev1_byte = image_to_byte_array(out_facev1)
        out_facev1_img = byte_to_base64_str(out_facev1_byte)


        out_facev2_byte = image_to_byte_array(out_facev2)
        out_facev2_img = byte_to_base64_str(out_facev2_byte)


        out_paprika_byte = image_to_byte_array(out_paprika)
        out_paprika_img = byte_to_base64_str(out_paprika_byte)


    
    return render_template("success.html", name = f.filename,
                            real = real_image,
                            celeba = out_celeba_img,
                            facev1 = out_facev1_img,
                            facev2 = out_facev2_img,
                            paprika = out_paprika_img)

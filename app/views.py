from flask import *
from app import app
from PIL import Image
from urllib import response
#from AnimeGanv2 import model
from os import environ as env
from .AnimeGanv2 import model
from .db import byte_to_base64_str,image_to_byte_array

# app = Flask(__name__)



app.config['UPLOAD_FOLDER'] = env['UPLOAD_FOLDER']
app.config['MAX_CONTENT_LENGTH'] = int(env['MAX_CONTENT_LENGTH'])

app.config['CARTOON_IMAGE_FOLDER'] = env['CARTOON_IMAGE_FOLDER']



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
        # real_image_id = upload_real_image(f,f.filename)
        img = Image.open(f.stream).convert("RGB")
     
        # print("Original Image shape: {}".format(img.size))
        # print("real imgae id: {}".format(real_image_id))
        # real_image = get_real_image(real_image_id)
        real_image_byte = image_to_byte_array(img)
        real_image = byte_to_base64_str(real_image_byte)

        out_celeba, out_facev1, out_facev2, out_paprika = model(img)

        out_celeba_byte = image_to_byte_array(out_celeba)
        # print("Output Image Shape: {}".format(out_celeba.size))
        # out_celeba_data = dict({
        #     "filename":"celeba_output.jpg",
        #     "shape": np.asarray(out_celeba).shape,
        #     "image": out_celeba_byte
        # })
        # out_celeba_id = upload_cartoon_image(out_celeba_data)
        # print("Cartoon Image id: {}".format(out_celeba_id))
        out_celeba_img = byte_to_base64_str(out_celeba_byte)


        out_facev1_byte = image_to_byte_array(out_facev1)
        # print("Output Image Shape: {}".format(out_facev1.size))
        # out_facev1_data = dict({
        #     "filename":"facev1_output.jpg",
        #     "shape": np.asarray(out_facev1).shape,
        #     "image": out_facev1_byte
        # })
        # out_facev1_id = upload_cartoon_image(out_facev1_data)
        # print("Cartoon Image id: {}".format(out_facev1_id))
        out_facev1_img = byte_to_base64_str(out_facev1_byte)


        out_facev2_byte = image_to_byte_array(out_facev2)
        # print("Output Image Shape: {}".format(out_facev2.size))
        # out_facev2_data = dict({
        #     "filename":"facev2_output.jpg",
        #     "shape": np.asarray(out_facev2).shape,
        #     "image": out_facev2_byte
        # })
        # out_facev2_id = upload_cartoon_image(out_facev2_data)
        # print("Cartoon Image id: {}".format(out_facev2_id))
        out_facev2_img = byte_to_base64_str(out_facev2_byte)


        out_paprika_byte = image_to_byte_array(out_paprika)
        # print("Output Image Shape: {}".format(out_paprika.size))
        # out_paprika_data = dict({
        #     "filename":"paprika_output.jpg",
        #     "shape": np.asarray(out_paprika).shape,
        #     "image": out_paprika_byte
        # })
        # out_paprika_id = upload_cartoon_image(out_paprika_data)
        # print("Cartoon Image id: {}".format(out_paprika_id))
        # out_paprika_img = get_cartoon_image(out_paprika_id)
        out_paprika_img = byte_to_base64_str(out_paprika_byte)


    
    return render_template("success.html", name = f.filename,
                            real = real_image,
                            celeba = out_celeba_img,
                            facev1 = out_facev1_img,
                            facev2 = out_facev2_img,
                            paprika = out_paprika_img)

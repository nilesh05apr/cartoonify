from ast import Bytes, Str
import io
from typing import Dict
import gridfs
import codecs
import numpy as np
from PIL import Image
from pymongo import MongoClient
from os import environ as env



# mc = MongoClient(env['DB_URL'])


# real_image_db = mc.get_database('REAL_DB')
# cartton_image_db = mc.get_database('CARTOON_DB')
# meta = mc.get_database('METADATA')


# r_fs = gridfs.GridFS(real_image_db)
# c_fs = gridfs.GridFS(cartton_image_db)

# def upload_real_image(image: Image, filename: Str) -> id:
#     _id = r_fs.put(data=image,name=filename)
#     image = Image.open(image.stream).convert('RGB')
#     metadata = {
#         "ImageId" : _id,
#         "shape":image.size
#     }
#     meta.images_metadata.insert_one(metadata)
#     return _id


# def upload_cartoon_image(image_data: Dict) -> id:
#     _id = c_fs.put(data=image_data['image'],name=image_data['filename'])
#     metadata = {
#         "ImageId" : _id,
#         "shape":image_data['shape']
#     }
#     meta.images_metadata.insert_one(metadata)
#     return _id


# def get_real_image(_id:id) -> Str:
#     image = r_fs.get(_id)
#     # print("Image type real:{}".format(type(image)))
#     base64_data = codecs.encode(image.read(),'base64')
#     r_image = base64_data.decode('utf-8')
#     # print("Type of r_image: {}".format(type(r_image)))
#     return r_image


# def get_cartoon_image(_id:id) -> Str:
#     image = c_fs.get(_id)
#     base64_data = codecs.encode(image.read(),'base64')
#     c_image = base64_data.decode('utf-8')
#     print("Type of c_image:{}".format(type(c_image)))
#     return c_image



def image_to_byte_array(image: Image) -> bytes:
  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format='PNG')
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr

def byte_to_base64_str(bytes: Bytes) -> Str:
    base64_data = codecs.encode(bytes,'base64')
    img_str = base64_data.decode('utf-8')
    return img_str
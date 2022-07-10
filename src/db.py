import gridfs
import codecs
import numpy as np
from PIL import Image
from pymongo import MongoClient

mc = MongoClient("mongodb+srv://admin:admin@cluster0.5wtig.mongodb.net/Cluster0?retryWrites=true&w=majority")
real_image_db = mc.get_database('REAL_DB')
cartton_image_db = mc.get_database('CARTOON_DB')
meta = mc.get_database('METADATA')


r_fs = gridfs.GridFS(real_image_db)
c_fs = gridfs.GridFS(cartton_image_db)

def upload_real_image(image,filename):
    _id = r_fs.put(data=image,name=filename)
    image = Image.open(image.stream).convert('RGB')
    metadata = {
        "id" : _id,
        "shape":image.size
    }
    meta.images_metadata.insert_one(metadata)
    return _id


def upload_cartoon_image(image,filename):
    _id = c_fs.put(data=image,name=filename)
    image = Image.open(image.stream).convert('RGB')
    metadata = {
        "id" : _id,
        "shape":image.size
    }
    meta.images_metadata.insert_one(metadata)
    return _id


def get_real_image(_id):
    image = r_fs.get(_id)
    # print(image)
    base64_data = codecs.encode(image.read(),'base64')
    r_image = base64_data.decode('utf-8')
    return r_image


def get_cartoon_image(_id):
    image = c_fs.get(_id)
    base64_data = codecs.encode(image.read(),'base64')
    c_image = base64_data.decode('utf-8')
    return c_image
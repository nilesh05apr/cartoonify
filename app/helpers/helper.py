import io
import codecs
from PIL import Image
from ast import Bytes, Str

def image_to_byte_array(image: Image) -> bytes:
  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format='PNG')
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr

def byte_to_base64_str(bytes: Bytes) -> Str:
    base64_data = codecs.encode(bytes,'base64')
    img_str = base64_data.decode('utf-8')
    return img_str
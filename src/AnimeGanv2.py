from PIL import Image
import torch

# https://github.com/bryandlee/animegan2-pytorch
# load models
model_celeba = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="celeba_distill")
model_facev1 = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v1")
model_facev2 = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v2")
model_paprika = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="paprika")

face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint", size=512)

# INPUT_IMG = "20190831_084825.jpg" # input_image jpg/png 
# img = Image.open(INPUT_IMG).convert("RGB")


def model(img):
    img = Image.open(img).convert("RGB")
    out_celeba = face2paint(model_celeba, img)
    out_facev1 = face2paint(model_facev1, img)
    out_facev2 = face2paint(model_facev2, img)
    out_paprika = face2paint(model_paprika, img)
    return out_celeba,out_facev1,out_facev2,out_paprika

# i1,i2,i3,i4 = model(img)

# i1.save('i1.jpg')

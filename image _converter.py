#!/usr/bin/env python3
#sizing photo pixel
import os
from PIL import Image

#   Size: Change image resolution from 3000x2000 to 600x400 pixel
#   Format: Change image format from .TIFF to .JPEG
path='supplier-data/images'#path dictionaries that file in
for image in os.listdir(path):
  filename=os.path.splitext(image)[0] #separate filename and extention
  if filename.isnumeric(): #to check that filename is numeric
    im=Image.open(path+'/'+image).convert("RGB") #open file and transform it into RGB, it must do
    im.resize((600,400)).save(path+'/{}.jpeg'. format(filename)) #resize file, we also can rotate the photo with command im.rotate(angle)
  else: pass

print("image files has been resized")

#!/usr/bin/env python3
#for uploading photo to localhost

import requests #modul for requesting to access the localhost
import os

url = "http://localhost/upload/" #localhost
path='supplier-data/images' #images directory
for image in os.listdir(path):
  if '.jpeg' in image:
    with open(path+"/"+image, 'rb') as opened:
      r=requests.post(url, files={'file': opened}) #request for post

print('images have been uploaded')

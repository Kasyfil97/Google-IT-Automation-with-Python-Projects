#! /usr/bin/env python3
#post descriptions to localhost

import os
import requests

key=['name','weight','description']
txt_path='supplier-data/descriptions'
for file in os.listdir(txt_path):
  item={}
  count=0
  with open(txt_path+'/'+file,'r') as txtfile:
    for line in txtfile:
#      print(line.replace("\n",""))
      if 'lbs' in line:
        item[key[count]]= int(line.replace(' lbs',""))
#        print(int(line.replace(' lbs',"")))
      elif line.isspace(): #to pass line that containes just space
        continue
      else:
#        print(line)
        item[key[count]]=line.replace("\n","")
      count+=1
    image_file_name=os.path.splitext(file)[0]
    item['image_name']=image_file_name+".jpeg" #adding image part into dictionary
#    print(item)
    response=requests.post('http://34.136.197.48/fruits/', json=item)
    if not response.ok:
      raise Exception("Failed, status code: {} in file: {}", format(response.status_code,file)) #to check error files and their status code
    print("descriptions Added")

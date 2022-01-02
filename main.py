#!/usr/bin/env python3
#generate fluid report pdf and sent it by email

import emails
import os
import sys
from datetime import date
import reports

def load_data(list):
"""function for making list with format name: dan weight:"""
  main=[]
  for part in list:
    text="name: {}<br/>weight: {}\n". format(part['name'],part['weight'])
    main.append(text)
  return main

def sentences(fluit_path):
  """fucntion for separating line in file and substituting them into dictionary and append them into list"""
  main=[]
  key=['name','weight','description']
  for file in os.listdir(fluit_path):
   item={}
   count=0
   with open(fluit_path+'/'+file,'r') as txtfile:
     for line in txtfile:
#      print(line.replace("\n",""))
#       if 'lbs' in line:
#         item[key[count]]= int(line.replace(' lbs',""))
#        print(int(line.replace(' lbs',"")))
       if line.isspace():
         continue
       else:
#        print(line)
         item[key[count]]=line.replace("\n","")
       count+=1
   main.append(item)
  return main

def main(argv):
#generate pdf part
  path='supplier-data/descriptions'
  now_date=date.today().strftime("%B %d, %Y")
  filename="/tmp/processed.pdf"
  title="Processed Update on "+now_date+'\n'
  Sentences=sentences(path)
  body="<br/><br/>".join(load_data(Sentences))
  reports.generate(filename,title,body)
  print('pdf has been generated')
#  print(body)
#send email
  sender = "automation@example.com"
  receiver = "student-00-3e4ad8c2e8b4@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send(message)
  print('Email has been sent')

if __name__ == "__main__":
  main(sys.argv)

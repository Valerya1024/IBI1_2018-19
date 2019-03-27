# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:46:28 2019

@author: surface
"""
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

txt_file = open('body.txt','r')
body = txt_file.read()

csv_file = open('address_information1.csv','r')
file = csv_file.read()

mail_host="smtp.zju.edu.cn"
mail_user="3180111***@zju.edu.cn"
mail_pass="********" 

sender = '3180111***@zju.edu.cn'

rows = re.split(r'[\n]',file)
names=[]
addresses=[]
subjects=[]

for i in range(1,len(rows)):
    info = re.split(r'[,]',rows[i])
    if '.com' in info[1]:
        addresses.append(info[1])
        print(info[1]+' :Correct Address!')
    else:
        print(info[1]+' :Wrong Address!')
        continue
    
    names.append(info[0])
    subjects.append(info[2])
    
print("From: "+sender+'\nPassword: '+mail_pass)
    
for i in range(len(addresses)):

    receivers = addresses[i]
    name=names[i]
    subject=subjects[i]
    
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header("824", 'utf-8')
    message['To'] =  Header(name, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
 
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    
    print("Mail sent successfully!")

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

csv_file = open('address_information.csv','r')
file = csv_file.read()

mail_host="smtp.zju.edu.cn"
mail_user="3180111439@zju.edu.cn"
mail_pass="********"

sender = '3180111439@zju.edu.cn'

rows = re.split(r'[\n]',file)
names=[]
addresses=[]
subjects=[]

csv_file.close()
txt_file.close()

for i in range(1,len(rows)):
    info = re.split(r'[,]',rows[i])
    if re.match(r'\w+@\w+\.\w+',info[1]):
        addresses.append(info[1])
        names.append(info[0])
        subjects.append(info[2])
        print(info[1]+' :Correct Address!')
    else:
        print(info[1]+' :Wrong Address!')
    
print("From: "+sender+'\nPassword: '+mail_pass)
    
for i in range(len(addresses)):

    receivers = addresses[i]
    name=names[i]
    subject=subjects[i]
    body_r=re.sub(r'User',name,body)

    message = MIMEText(body_r, 'plain', 'utf-8')
    message['From'] = Header('Val', 'utf-8')
    message['To'] =  Header(name, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
 
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
    
        print("Mail sent successfully!")
        
    except smtplib.SMTPException:
        print ("Error! Can not send the email.")

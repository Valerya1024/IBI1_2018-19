# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:00:44 2019

@author: Valerya
"""

import os
import xml.dom.minidom
import pandas as pd
import matplotlib.pyplot as plt

def xml_to_cps():
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()

xml_to_cps()
os.system('CopasiSE.exe predator-prey.cps')

res = pd.read_csv('modelResults.csv')

res.plot(x='Time', y=['[A]','[B]'],label=['Predator (b=0.02, d=0.4)','Prey (b=0.1, d=0.02)'],figsize=(9,6))
plt.title('Time course')
plt.xlabel('time')
plt.ylabel('population size')
plt.legend(loc='upper right')
plt.show()

res.plot(x='[A]',y='[B]',figsize=(9,6))
plt.title('Limit cycle')
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.show()


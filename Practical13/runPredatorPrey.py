# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:00:44 2019

@author: Valerya

ERROR when generating modelResults.csv
surface@Desktop-Valerya MINGW64 ~/.spyder-py3/python_script/Practical_XII
$ CopasiSE.exe predator-prey.cps
COPASI 4.25 (Build 207)
The use of this software indicates the acceptance of the attached license.
To view the license please use the option: --license

File: predator-prey.cps
>EXCEPTION 2019-05-16T09:23:44<
XML (22): Duplicate XML Id 'Report_18' encountered in line '729'.
"""

import os
import xml.dom.minidom as minidom
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xmlTree = minidom.parse("predator-prey.xml")
xmlCollection = xmlTree.documentElement
parameters = xmlCollection.getElementsByTagName("parameter")

def xml_to_cps():
    
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    cpsTree = minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = minidom.parse("report_ref.xml")
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
            
    report18 = minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
    
def Plot():
    os.system('CopasiSE.exe predator-prey.cps')
    res = pd.read_csv('modelResults.csv')

    res.plot(x='Time', y=['[A]','[B]'],label=['Predator (b=0.02, d=0.4)','Prey (b=0.1, d=0.02)'],figsize=(9,6))
    plt.title('Time course')
    plt.xlabel('time')
    plt.ylabel('population size')
    plt.legend(loc='upper right')
    plt.savefig('Time_course.png')
    plt.show()

    res.plot(x='[A]',y='[B]',label='predator-prey',figsize=(9,6))
    plt.title('Limit cycle')
    plt.xlabel('predator population')
    plt.ylabel('prey population')
    plt.savefig('Limit_cycle.png')
    plt.show()
#5
def Change_value():
    for parameter in parameters:
        ID = parameter.getAttribute("id")
        parameter.setAttribute("value",input(ID+'='))
    xml_to_cps()
#6
def Random_value():
    n = input('run_times=')
    data = []
    k = []
    for i in range(int(n)):
        rnd = list(np.random.sample(4)) #generate 4 random value between 0 and 1
        for i in range(4):
            k.append(parameters[i].getAttribute("id"))
            parameters[i].setAttribute("value",rnd[i])
        xml_to_cps()
        os.system('CopasiSE.exe predator-prey.cps')
        res = pd.read_csv('modelResults.csv')
        data.append(rnd+[round(max(res['[A]'])),round(max(res['[B]']))])
    
    df = pd.DataFrame(data)
    df.columns=[k[0],k[1],k[2],k[3],'predator max','prey max']
    print(df)
    df.to_excel('random_k.xlsx', index=False)

x = input('Select function:\nA.default values B.change values C.random values\n')
if x == 'A':
    xml_to_cps()
    Plot()
elif x == 'B':
    Change_value()
    Plot()
elif x == 'C':
    Random_value()



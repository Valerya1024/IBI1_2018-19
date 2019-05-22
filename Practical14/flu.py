# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:04:07 2019

@author: Valerya
"""

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

df = pd.read_excel('Final_Fluview_Practical_dataset.xlsx')
df1 = df[['Virus Strain','Age','Gender','Hospitalized?','Swine Contact?','Attended Agricultural Event?']]
df1 = df1.dropna()
df1['H3N2v']=df1['Virus Strain'].map({'Influenza A H1N1v':0,'Influenza A H1N2v':0,'Influenza A H7N2':0,'Influenza A H3N2v':1})
df1['Age']=df1['Age'].map({'<18 Years':0,'>=18 Years':1})
df1['Gender']=df1['Gender'].map({'Male':1,'Female':0,'male':1,'female':0})
df1['Hospitalized?']=df1['Hospitalized?'].map({'Yes':1,'No':0,'no':0,'yes':1})
df1['Swine Contact?']=df1['Swine Contact?'].map({'Yes':1,'No':0,'no':0,'yes':1})
df1['Attended Agricultural Event?']=df1['Attended Agricultural Event?'].map({'Yes':1,'No':0,'no':0,'yes':1})

endog = df1['H3N2v']
exog = df1[['Age','Gender','Hospitalized?','Swine Contact?','Attended Agricultural Event?']]

exog = sm.add_constant(exog)
logit = smf.Logit(endog, exog)
result = logit.fit()
print(result.summary())
print('Odds ratios:')
print(np.exp(result.params))


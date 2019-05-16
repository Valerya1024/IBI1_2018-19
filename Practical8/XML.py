# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:05:41 2019

@author: surface
"""
import re
import xml.dom
import pandas as pd

DOM = xml.dom.minidom.parse('go_obo.xml')
obo = DOM.documentElement
genes = obo.getElementsByTagName('term')

def findchildren(id,children):
    for term in genes:
            parents = term.getElementsByTagName('is_a')
            for parent in parents:
                if parent.childNodes[0].data == id:
                    childid = term.getElementsByTagName('id')[0].childNodes[0].data
                    children.append(childid)
                    findchildren(childid,children)
    return len(children)
                
autophagosome = pd.DataFrame(columns = ['id','name','definition','childnodes'])

for term in genes:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    if re.search(r'autophagosome', defstr):
        id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        children = []
        autophagosome = autophagosome.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[findchildren(id,children)]}))

autophagosome.to_excel('autophagosome.xlsx', index=False)
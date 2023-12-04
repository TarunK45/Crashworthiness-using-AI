# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:04:39 2022

@author: user
"""

# -*- coding: utf-8 -*-

import numpy as np
from tensorflow import keras
bbb=[]
ccc=[]
eee=[]
fff=[]
def predict(x):
    model = keras.models.load_model('Modelrf')
    aa=model.predict(x)
    return(float(aa))
new_file=open('parameter angle.txt')
new_file2=open('parameter thickness.txt')
new_file3=open('parameter width.txt')
res_file=open('result3.txt','w')
for line in new_file:
    ext_line=line
    ext_w=ext_line.split()
    bbb.append((float(ext_w[0])+30)/60)
for line in new_file2:
    ext_line=line
    ext_w=ext_line.split()
    ccc.append((float(ext_w[0])-2)/3)
for line in new_file3:
    ext_line=line
    ext_w=ext_line.split()
    fff.append((float(ext_w[0])-2)/3)

for i in range (0,len(bbb)):
    xp=[bbb[i],ccc[i],fff[i]]
    xp=np.reshape(xp,(1,3))
    dd=predict(xp)
    eee.append(dd)
    res_file.write((repr((dd*20059.86)+1995.44))+"\n")
    
new_file.close()
new_file2.close()
new_file3.close()
res_file.close()






# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:09:52 2022

@author: MAINAK
"""
import numpy as np
from tensorflow import keras
b=[]
c=[]
e=[]
def predict(x):
    model = keras.models.load_model('ModelV2')
    a=model.predict(x)
    return(float(a))
new_file=open('parameter angle.txt')
new_file2=open('parameter thickness.txt')
res_file=open('result.txt','w')
for line in new_file:
    ext_line=line
    ext_w=ext_line.split()
    b.append(float(ext_w[0]))
for line in new_file2:
    ext_line=line
    ext_w=ext_line.split()
    c.append(float(ext_w[0]))

for i in range (0,len(b)):
    xp=[b[i],c[i]]
    xp=np.reshape(xp,(1,2))
    d=predict(xp)
    e.append(d)
    res_file.write(repr(d)+"\n")
    
new_file.close()
new_file2.close()
res_file.close()






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
f=[]
def predict(x):
    model = keras.models.load_model('Modelmass')
    a=model.predict(x)
    return(float(a))
new_file=open('parameter angle.txt')
new_file2=open('parameter thickness.txt')
new_file3=open('parameter width.txt')
res_file=open('result.txt','w')
for line in new_file:
    ext_line=line
    ext_w=ext_line.split()
    b.append((float(ext_w[0])+30)/60)
for line in new_file2:
    ext_line=line
    ext_w=ext_line.split()
    c.append((float(ext_w[0])-2)/3)
for line in new_file3:
    ext_line=line
    ext_w=ext_line.split()
    f.append((float(ext_w[0])-2)/3)
for i in range (0,len(b)):
    xp=[b[i],c[i],f[i]]
    xp=np.reshape(xp,(1,3))
    d=predict(xp)
    e.append(d)
    res_file.write((repr((d*0.00836)+0.0012))+"\n")
    
new_file.close()
new_file2.close()
new_file3.close()
res_file.close()






# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:09:52 2022

@author: MAINAK
"""
import numpy as np
from tensorflow import keras
bb=[]
cc=[]
ee=[]
ff=[]
def predict(x):
    model = keras.models.load_model('Modelenergy')
    aa=model.predict(x)
    return(float(aa))
new_file=open('parameter angle.txt')
new_file2=open('parameter thickness.txt')
new_file3=open('parameter width.txt')
res_file=open('result2.txt','w')
for line in new_file:
    ext_line=line
    ext_w=ext_line.split()
    bb.append((float(ext_w[0])+30)/60)
for line in new_file2:
    ext_line=line
    ext_w=ext_line.split()
    cc.append((float(ext_w[0])-2)/3)
for line in new_file3:
    ext_line=line
    ext_w=ext_line.split()
    ff.append((float(ext_w[0])-2)/3)

for i in range (0,len(bb)):
    xp=[bb[i],cc[i],ff[i]]
    xp=np.reshape(xp,(1,3))
    dd=predict(xp)
    ee.append(dd)
    res_file.write((repr((dd*7.048754361)+0.06213389121))+"\n")
    
new_file.close()
new_file2.close()
new_file3.close()
res_file.close()






# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:27:13 2024

@author: TANISHKA
"""

import numpy as np
import pickle

loadmodel=pickle.load(open('C:/Users/TANISHKA/Desktop/TanishaML/Diabetes','rb'))

input_data=(	89	,66,	23,	94	,28.1,	0.167,21,0)
array=np.asarray(input_data)
#reshape
inputreshape=array.reshape(1,-1)
std_data=scaler.transform(inputreshape)
print(std_data)
prediction=classifier.predict(std_data)
print(prediction)
if(prediction[0]==0):
  print("You are not diabetic ")
else:
  print("You are diabetic")
  

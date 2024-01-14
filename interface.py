# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:33:05 2024

@author: TANISHKA
"""

import pickle
import numpy as np
import streamlit as st

loadmodel=pickle.load(open('trained_model.sav','rb'))

def diabetes_prediction(input_data):

    array=np.asarray(input_data)
    #reshape
    inputreshape=array.reshape(1,-1)
    std_data=scaler.transform(inputreshape)
    print(std_data)
    prediction=classifier.predict(std_data)
    print(prediction)
    if(prediction[0]==0):
        
        return "You are not diabetic "
    else:
        
        return "You are diabetic"
      
def main():
    st.title('Diabetes prediction app for Women ')
    
    Pregnancies=st.text_input("Please enter number of pregnancies ")
    Glucose=st.text_input("Please enter your recent glucose level")
    Bloodpressure=st.text_input("Please enter your blood pressure value(recent)")
    Skinthickness=st.text_input("Please enter your skin thickness")
    Insulin=st.text_input("Please enter your insulin levels")
    BMI=st.text_input("Please enter your BMI level")
    DiabetesPedigree=st.text_input("Please enter your Diabetes Pedigree value")
    Age=st.text_input("Please enter your age in years")
    
    diagonsis=''
    if st.button("Diabetes test result"):
        diagonsis=diabetes_prediction([Pregnancies,Glucose,Bloodpressure,Skinthickness,Insulin,BMI,DiabetesPedigree,Age])
    st.success(diagonsis)


if __name__ =='__main__':
    main()

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:56:45 2023

@author: Anushka Gupta
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models

breast_cancer_model = pickle.load(open('breast_cancer_detection_model.sav', 'rb'))

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Breast Cancer Prediction',
                            'Diabetes Prediction'],
                           
                           icons = ['gender-female', 'activity'],
                           
                           default_index = 0)

# Breast Cancer Prediction Page
if(selected == 'Breast Cancer Prediction'):
    
    #page title
    st.title('Breast Cancer Prediction using ML')
    st.write('Enter the following details of the cell nuclei:')
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
   
    with col1:
       RadiusMean = st.text_input('Radius Mean')
       
    with col2:
       TextureMean = st.text_input('Texture Mean')
   
    with col3:
       SmoothnessMean = st.text_input('Smoothness Mean')
   
    with col1:
       CompactnessMean = st.text_input('Compactness Mean')
   
    with col2:
       SymmetryMean = st.text_input('Symmetry Mean')
   
    with col3:
       FractalDimensionMean = st.text_input('Fractal Dimension Mean')
   
    with col1:
       RadiusSE = st.text_input('Radius Standard Error')
       
    with col2:
       TextureSE = st.text_input('Texture Standard Error')
   
    with col3:
       SmoothnessSE = st.text_input('Smoothness Standard Error')
   
    with col1:
       CompactnessSE = st.text_input('Compactness Standard Error')
   
    with col2:
       SymmetrySE = st.text_input('Symmetry Standard Error')
   
    with col3:
       FractalDimensionSE = st.text_input('Fractal Dimension Standard Error')
       
    # code for Prediction
    cancer_diagnosis = ''
    
    # Prediction Button
    
    if st.button('Breast Cancer Test Result'):
        cancer_prediction = breast_cancer_model.predict([[RadiusMean, TextureMean, SmoothnessMean,
                                                                    CompactnessMean, SymmetryMean, FractalDimensionMean,
                                                                    RadiusSE, TextureSE, SmoothnessSE, CompactnessSE,
                                                                    SymmetrySE, FractalDimensionSE]])
        
        if (cancer_prediction[0] == 1):
            cancer_diagnosis = 'The person has Breast Cancer'
            
        else:
            cancer_diagnosis = 'The person does not have Breast Cancer'
            
    st.success(cancer_diagnosis)
    

# Diabetes Prediction Page    
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
   
    with col1:
       Pregnancies = st.text_input('Number of Pregnancies')
       
    with col2:
       Glucose = st.text_input('Glucose Level')
   
    with col3:
       BloodPressure = st.text_input('Blood Pressure value')
   
    with col1:
       SkinThickness = st.text_input('Skin Thickness value')
   
    with col2:
       Insulin = st.text_input('Insulin Level')
   
    with col3:
       BMI = st.text_input('BMI value')
   
    with col1:
       DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
   
    with col2:
       Age = st.text_input('Age of the Person')
       
       
    # code for Prediction
    diab_diagnosis = ''
    
    # Prediction Button
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                                   Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is not Diabetic'
            
    st.success(diab_diagnosis)
    
    
#import library
import numpy as np
import seaborn as sns 
import pandas as pd
import pickle as pkl
import streamlit as st 
#import model
model = pkl.load(open('model/MIPM.pkl', 'rb'))

st.header('**Medical Insurence Premium prediction System**')

#get input data
gender = st.selectbox('**Choose Gender**',['Female','Male'])
smoker = st.selectbox('**Are you a smoker** ?',['Yes','No'])
region = st.selectbox('**Choose Region**', ['SouthEast','SouthWest','NorthEast','NorthWest'])
age = st.slider('**Enter Age**', 1 , 100)
bmi = st.slider('**Enter BMI**', 1 , 100)
children = st.slider('**Choose No of Childrens**', 0, 7)

#convert categories columns to numerical values
if st.button('**Predict your Premium**'):
    if gender == 'Female':
     gender = 0
    else:
        gender = 1

    if smoker == 'Yes':
        smoker = 1
    elif smoker == 'No':
        smoker = 0
    if region == 'SouthEast':
        region = 0
    if region == 'SouthWest':
        region = 1
    if region == 'NorthEast':
        region = 2
    else:
        region = 3
    # collect input data from some source
    input_data = (age, gender, bmi, children,smoker, region)
    #convert the input_data tuple into a NumPy array
    input_data_array = np.asarray(input_data)
    # reshapes the input_data_array to converts the one-dimensional array into a row vector
    input_data_array = input_data_array.reshape(1,-1)
    #predicts insurance premiums based on the given data
    predicted_prem = model.predict(input_data_array)
    # diplay predicted value in USD Dollars
    display_string = '**Your Premium Insurance is:** '+ str(round(predicted_prem[0],2)) + ' **USD Dollars**'
    #display the text “bold text” in bold on the page
    st.markdown(display_string)
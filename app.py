import pickle
import streamlit as st
from _streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model=pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))

//sidebar for navigation
with st.sidebar:
	selected=option_menu('Multiple Disease Prediction System',
	                   ['Diabetes Prediction',
					   Heart Disease Prediction,
					   Parkinsons Prediction],
					   icons=['activity','heart','person'],
					   default_index=0)
//Diabetes prediction page
if(selected =='Diabetes Prediction')

//page title
st.title('Diabetes Prediction Using Machine Learning')

//getting input data from the user
col1,col2,col3=columns.st(3)

with col1:
           Pregnancies= st.text_input('Number of Pregnancies')
with col2:
           Glucose= st.text_input('Glucose level')
with col3:
           BloodPressure= st.text_input('Blood Pressure value')		   		   					   
					   
with col1:
           SkinThickness= st.text_input('Skin Thickness Value')
with col2:
           Insulin= st.text_input('Insulin level')
with col3:
           BMI= st.text_input('BMI Value')
		   		   		   					   
					   
					   
					   
					   
					   
					   
					   
					   

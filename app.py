
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import importlib.util

# Load the uploaded Python file
file_path = 'preventive_measures_using_ann.py'
spec = importlib.util.spec_from_file_location("preventive_measures", file_path)
preventive_measures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preventive_measures)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Preventive Measures System',
                           ['Preventive Measures'],
                           icons=['heart'],
                           default_index=0)

# Preventive Measures Page
if selected == 'Preventive Measures':
    st.title('Preventive Measures using Rule-based Recommendations')

    # Collect user inputs
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        sex = st.selectbox('Sex', ['Male', 'Female'])
        smoke = st.selectbox('Do you smoke?', ['Yes', 'No'])

    with col2:
        alcohol = st.selectbox('Do you consume alcohol?', ['Yes', 'No'])
        exercise_freq = st.selectbox('Exercise Frequency', ['Never', 'Sometimes', 'Regularly'])
        bmi = st.text_input('BMI')

    with col3:
        bmi_numeric = st.selectbox('BMI Numeric', ['Underweight', 'Normal weight', 'Overweight', 'Obesity'])

    user_data = {
        'Age': age,
        'Sex': sex,
        'Smoke': 1 if smoke == 'Yes' else 0,
        'Alcohol': 1 if alcohol == 'Yes' else 0,
        'Exercise Frequency': ['Never', 'Sometimes', 'Regularly'].index(exercise_freq),
        'BMI': bmi,
        'BMI_numeric': ['Underweight', 'Normal weight', 'Overweight', 'Obesity'].index(bmi_numeric)
    }

    recommendations = preventive_measures.generate_recommendations(user_data)

    if st.button('Get Recommendations'):
        st.subheader('Recommendations:')
        for rec in recommendations:
            st.write('- ' + rec)

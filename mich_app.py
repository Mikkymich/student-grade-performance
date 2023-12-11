# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:12:23 2023

@author: user
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
from joblib import load
from sklearn.preprocessing import LabelEncoder

# Load the pre-trained model
model = load('michael_model.joblib')

# Label encoders
label_encoders = {
    'sex': LabelEncoder(), 
    'address': LabelEncoder(),
    'famsize': LabelEncoder(), 
    'Pstatus': LabelEncoder(),
    'Mjob': LabelEncoder(), 
    'Fjob': LabelEncoder(),
    'reason': LabelEncoder(), 
    'guardian': LabelEncoder(),
    'schoolsup': LabelEncoder(), 
    'famsup': LabelEncoder(),
    'paid': LabelEncoder(), 
    'activities': LabelEncoder(),
    'nursery': LabelEncoder(), 
    'higher': LabelEncoder(),
    'internet': LabelEncoder(), 
    'romantic': LabelEncoder()
}

def encode_features(data):
    for column, encoder in label_encoders.items():
        data[column] = encoder.transform(data[column])
    return data

# Function to make predictions
def predict_grade(data):
    data = encode_features(data)
    prediction = model.predict([data])[0]
    return prediction

# Streamlit app
def main():
    # Load custom CSS
    st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)

    st.title("Student Performance Prediction")

    # Input form
    st.sidebar.header("User Input")
    sex = st.sidebar.radio("Gender", ["male", "female"])
    age = st.sidebar.slider("Age", min_value=15, max_value=22, value=18)
    # Add other input fields based on your data structure

    submitted = st.sidebar.button("Submit")

    if submitted:
        # Create a dictionary with the user input
        user_input = {
            'sex': sex,
            'age': age,
            # Add other input fields based on your data structure
        }

        # Create a DataFrame from the user input
        input_df = pd.DataFrame([user_input])

        # Make prediction
        prediction = predict_grade(input_df)

        # Display prediction
        st.subheader("Prediction Result")
        st.write(f"The student is likely to have a grade of {prediction} next semester.")

if __name__ == "__main__":
    main()

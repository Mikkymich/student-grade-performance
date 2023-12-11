# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:09:37 2023

@author: Windows
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from student_info import StudentInfo
import numpy as np
from joblib import load
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler



# 2. Create the app object
app = FastAPI()
model = load('michael_model.joblib')

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'GOMYCODE IN-HOUSE HACKATHON'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To our solution': f'{name}'}

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


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted performance with the confidence
@app.post('/predict')
def predict_grade(data:StudentInfo):
    data = data.dict()
    sex = data['sex']
    age = data['age']
    address = data['address']
    famsize = data['famsize']
    Pstatus = data['Pstatus']
    Medu = data['Medu']
    Fedu = data['Fedu']
    Mjob = data['Mjob']
    Fjob = data['Fjob']
    reason = data['reason']
    guardian = data['guardian']
    traveltime = data['traveltime']
    studytime = data['studytime']
    failures = data['failures']
    schoolsup = data['schoolsup']
    famsup = data['famsup']
    paid = data['paid']
    activities = data['activities']
    nursery = data['nursery']
    higher = data['higher']
    internet = data['internet']
    romantic = data['romantic']
    famrel = data['famrel']
    freetime = data['freetime']
    goout = data['goout']
    Dalc = data['Dalc']
    Walc = data['Walc']
    health = data['health']
    absences = data['absences']
    G1 = data['G1']
    G2 = data['G2']
    
    
    # Encode categorical column(s)
    encoded_sex = label_encoders['sex'].transform([sex])[0]
    encoded_address = label_encoders['address'].transform([address])[0]
    encoded_famsize = label_encoders['famsize'].transform([famsize])[0]
    encoded_guardian = label_encoders['guardian'].transform([guardian])[0]
    encoded_Pstatus = label_encoders['Pstatus'].transform([Pstatus])[0]
    encoded_Mjob = label_encoders['Mjob'].transform([Mjob])[0]
    encoded_Fjob = label_encoders['Fjob'].transform([Fjob])[0]
    encoded_reason = label_encoders['reason'].transform([reason])[0]
    encoded_schoolsup = label_encoders['schoolsup'].transform([schoolsup])[0]
    encoded_famsup = label_encoders['famsup'].transform([famsup])[0]
    encoded_paid = label_encoders['paid'].transform([paid])[0]
    encoded_activities = label_encoders['activities'].transform([activities])[0]
    encoded_nursery = label_encoders['nursery'].transform([nursery])[0]
    encoded_higher = label_encoders['higher'].transform([higher])[0]
    encoded_internet = label_encoders['internet'].transform([internet])[0]
    encoded_romantic = label_encoders['romantic'].transform([romantic])[0]
 
 
   # Convert data to the same type as the model expects
    data_for_prediction = [
       encoded_sex, age, encoded_address,encoded_address,encoded_famsize,encoded_guardian, Medu,Fedu,
       encoded_Mjob,encoded_Fjob,encoded_reason,encoded_schoolsup,encoded_famsup,encoded_paid,encoded_activities,encoded_nursery,encoded_higher,
       encoded_internet,encoded_romantic,traveltime,studytime,failures,famrel,freetime,goout,Dalc,Walc,health,
       absences,G1,G2,encoded_Pstatus
   ]
    
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = model.predict([[data_for_prediction]])
    print(f'The student is lkely to have a grade of {prediction}, next semester.')
    
# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == "__main__":
    import uvicorn

    # Run the API with uvicorn
    # Will run on http://127.0.0.1:8000
uvicorn.run(app, host='127.0.0.1', port=8000)

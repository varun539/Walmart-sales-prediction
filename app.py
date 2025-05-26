import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib

# Load the trained model
model = joblib.load('final_rf_model.pkl')

st.title("🛒 Weekly Sales Prediction App")
st.write("Fill in the details below to predict the weekly sales:")

# Input fields for each feature
Store = st.number_input('Store', min_value=1, step=1)
Dept = st.number_input('Department', min_value=1, step=1)
IsHoliday = st.selectbox('Is it a Holiday?', ['No', 'Yes'])
Temperature = st.number_input('Temperature (in °F)')
Fuel_Price = st.number_input('Fuel Price (in USD)')
MarkDown1 = st.number_input('MarkDown1', value=0.0)
MarkDown2 = st.number_input('MarkDown2', value=0.0)
MarkDown3 = st.number_input('MarkDown3', value=0.0)
MarkDown4 = st.number_input('MarkDown4', value=0.0)
MarkDown5 = st.number_input('MarkDown5', value=0.0)
CPI = st.number_input('CPI')
Unemployment = st.number_input('Unemployment rate')
Type = st.selectbox('Store Type', ['A', 'B', 'C'])
Size = st.number_input('Store Size')
Year = st.number_input('Year', min_value=2010, max_value=2025, step=1)
Month = st.number_input('Month', min_value=1, max_value=12, step=1)
Week = st.number_input('Week Number', min_value=1, max_value=52, step=1)
DayOfWeek = st.number_input('Day of the Week (0=Sun, 6=Sat)', min_value=0, max_value=6, step=1)
IsWeekend = st.selectbox('Is it a Weekend?', ['No', 'Yes'])

# Extra field to match training features
SalesPerSize = st.number_input('Sales Per Size', value=0.0)

# Convert categorical inputs
IsHoliday = 1 if IsHoliday == 'Yes' else 0
IsWeekend = 1 if IsWeekend == 'Yes' else 0
Type_mapping = {'A': 0, 'B': 1, 'C': 2}
Type = Type_mapping[Type]

# Arrange input features in the correct order
input_data = np.array([[
    Store, Dept, IsHoliday, Temperature, Fuel_Price,
    MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5,
    CPI, Unemployment, Type, Size,
    Year, Month, Week, DayOfWeek, IsWeekend,
    SalesPerSize
]])

# Predict
if st.button('Predict Weekly Sales'):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Weekly Sales: ${prediction:,.2f}")

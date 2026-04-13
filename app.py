import streamlit as st
import pandas as pd
import pickle

# Load your trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Grievance AI")

# Add your input fields here
user_input = st.text_input("Enter grievance text")

if st.button("Predict"):
    result = model.predict([user_input])
    st.write("Result:", result)
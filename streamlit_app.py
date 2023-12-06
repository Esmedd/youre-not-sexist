import streamlit as st
import requests
import time
import random

st.title("Sexism Prediction App")
st.write("This app predicts if a statement is sexist or not")

entry_text = st.text_input("Statement", "women should stay in the kitchen")

if st.button("Is this sexist?"):
    data = {
        "text": entry_text}

    api_endpoint = 'http://localhost:8000/predict'
    response = requests.post(api_endpoint, json=data)


    # Display prediction result
    if response.status_code == 200:

        prediction = response.json()[1]

        def determine_result(prediction):
            return "Sexist" if prediction > 0.5 else "Not Sexist"

        binary = determine_result(prediction)

        if binary == "Sexist":
            st.success(f"Oh no, this phrase is {binary} :( (With {prediction*100}% certainty...)")
        elif binary == "Not Sexist" and prediction > 0.3:
            st.success(f"This phrase is {binary}! (However we detected a {prediction*100}% probability of sexism... We reccommend rewriting your phrase.)")
        else:
            st.success(f"Congratulations, you're phrase is {binary}! (With {prediction*100}% certainty...)")
    else:
        st.error("Error predicting sexism. Please check your input parameters.")

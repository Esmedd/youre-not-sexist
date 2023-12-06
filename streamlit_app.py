import streamlit as st
import requests
import time
import random
from sexism_generator import *

st.title("Sexism Prediction App")
st.write("This app predicts if a statement is sexist or not")


if st.button("Generate Random Sexist Phrase"):
        phrase = generate_sexism(phrases=1)[0]
        st.text_area("Generated Phrase", phrase, key="generated_phrase")


entry_text = st.text_input("Statement", "paste your sexist phrase here")

if st.button("Is this sexist?"):
    data = {
        "text": entry_text}

    # Show spinner while waiting for API response
    with st.spinner("Loading the model..."):

        api_endpoint = 'https://image-yns-hnmgjahexq-uc.a.run.app/predict'
        response = requests.get(api_endpoint, params=data)
        nice = response.json()

    # Display prediction result
    if response.status_code == 200:

        prediction = round(list(nice.values())[0], 3)

        def determine_result(prediction):
            return "Sexist" if prediction > 0.4 else "Not Sexist"

        binary = determine_result(prediction)

        if binary == "Sexist":
            st.error(f"Oh no, this phrase is {binary} 😔 \r\n (With {prediction*100}% certainty...)")
        elif binary == "Not Sexist" and prediction > 0.25:
            st.warning(f"This phrase is {binary}! \r\n However we detected a {prediction*100}% probability of sexism... \r\n We recommend rewriting your phrase.")
        else:
            st.success(f"Congratulations, you're phrase is {binary}! 🥳 \r\n with {prediction*100}% certainty...")
    else:
        st.error("Error predicting sexism. Please check your input parameters.")

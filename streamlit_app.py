import streamlit as st
import requests
import time
import random
from sexism_generator import *

st.title("You're Not Sexist: Sexism Detection Tool")
st.write("Our fine-tuned BERT model is a sophisticated tool designed to detect sexism in texts. By leveraging advanced NLP techniques, contextual embeddings, and extensive pre-training, we aim to contribute to the ongoing efforts in addressing biases in language.")
st.write("By Arnaud Blanchard, Carina Prunkl, Marion Gagnadre & Elizabeth den Dulk")

if st.button("Generate Random Sexist Phrase"):
        phrase = generate_sexism(phrases=1)[0]
        st.text_area("Generated Phrase", phrase, key="generated_phrase")


entry_text = st.text_input("Statement", "Paste your sexist phrase here!")

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
            st.success(f"Congratulations, you're phrase is {binary}! 🥳")
    else:
        st.error("Error predicting sexism. Please check your input parameters.")

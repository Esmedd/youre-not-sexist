import streamlit as st
import requests

st.title("Sexism Prediction App")
st.write("This app predicts if a statement is sexist or not")

entry_text = st.text_input("Statement", "women should stay in the kitchen")

if st.button("Is this sexist?"):
    # Prepare data for API request
    data = {
        "text": entry_text}
    # Replace 'YOUR_API_ENDPOINT' with the actual endpoint of your API
    api_endpoint = 'YOUR_API_ENDPOINT'

    # Make API request
    response = requests.post(api_endpoint, json=data)

    # Display prediction result
    if response.status_code == 200:
        prediction = response.json()[1]
        st.success(f"There is a {prediction}% probability that this is sexist")
    else:
        st.error("Error predicting sexism. Please check your input parameters.")

# Note: Replace 'YOUR_API_ENDPOINT' with the actual endpoint of your API

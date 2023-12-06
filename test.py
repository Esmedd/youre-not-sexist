import streamlit as st
import requests
import time
import random

st.title("Sexism Prediction App")
st.write("This app predicts if a statement is sexist or not")

entry_text = st.text_input("Statement", "women should stay in the kitchen")
button = st.button("Is this sexist?")


if st.button("Is this sexist?"):
    # data = {
    #     "text": entry_text}
    # Replace 'YOUR_API_ENDPOINT' with the actual endpoint of your API
    #api_endpoint = 'YOUR_API_ENDPOINT'

    # Make API request
    #response = requests.post(api_endpoint, json=data)
    response = random.random()

    # Display prediction result
    #if response.status_code == 200:

    if response > 0:
        #prediction = response.json()[1]
        prediction = response

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

# Note: Replace 'YOUR_API_ENDPOINT' with the actual endpoint of your API




# import streamlit as st
# import requests

# # Function to simulate an API call
# def simulate_api_call():
#     # Replace this with your actual API call
#     # For demonstration purposes, using a random value between 0 and 1
#         # Prepare data for API request
#     data = {
#         "text": entry_text}
#     # Replace 'YOUR_API_ENDPOINT' with the actual endpoint of your API
#     api_endpoint = 'YOUR_API_ENDPOINT'

#     # Make API request
#     response = requests.post(api_endpoint, json=data)
#     return response.json()[1]

# # Function to determine the result based on the API response
# def determine_result(api_response):
#     return "Sexist" if api_response > 0.5 else "Not Sexist"

# # Streamlit app
# def main():
#     st.title("Sexism Prediction App")
#     st.write("This app predicts if a statement is sexist or not")

#     # UI components
#     text_input = st.text_input("Statement", "e.g. women should stay in the kitchen")
#     button = st.button("Is this sexist?")

#     if button and text_input:
#         # Show spinner while waiting for API response
#         with st.spinner("Loading the model..."):
#             # Simulate API call
#             api_response = simulate_api_call()

#         # Determine result based on API response
#         result = determine_result(api_response)

#         # Display result
#         st.success(f"The verdict: {result}")

# if __name__ == "__main__":
#     main()

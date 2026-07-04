import streamlit as st

st.set_page_config(page_title="Addition App")

st.title("Simple Addition Application")

st.write("Deployed from GCP Cloud Shell to GitHub and Streamlit Cloud")

number1 = st.number_input("Enter first number")

number2 = st.number_input("Enter second number")

if st.button("Calculate Addition"):
    result = number1 + number2
    st.success("Addition Result = " + str(result))

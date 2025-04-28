import requests
import streamlit as st


st.markdown("<h2 style='color: gold;'>Interview Question Generator</h2>", unsafe_allow_html=True)

experience = st.text_input("Enter years of Experience")
designation = st.text_input("Enter the Designation")

if st.button("Generate Questions"):
    payload = {"experience": experience, "designation": designation}
    response = requests.post("http://127.0.0.1:8000/generate-questions", json=payload)
    
    if response.status_code == 200:
        questions = response.json()["questions"]
        st.write(questions['text'])
    else:
        st.error("Something went wrong.")

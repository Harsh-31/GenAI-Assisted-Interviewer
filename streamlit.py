import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os

# API Key
api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.markdown("<h2 style='color: gold;'>Interview Question Generator</h2>", unsafe_allow_html=True)

experience = st.text_input("Enter years of Experience")
designation = st.text_input("Enter the Designation")

if st.button("Generate Questions"):
    llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-4o", temperature=0.1)

    prompt_template = ChatPromptTemplate.from_template(
        """You are an expert interviewer.
        Create 10 high-quality interview questions for a candidate applying for the role of '{designation}'
        with {experience} years of experience.

        The question pattern should be:
        A) Basic questions - 10-12
        B) Scenario based questions - 3-4
        C) Approach based questions - 5-6
        D) OOPs Concept questions - 7-8
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.invoke({"experience": experience, "designation": designation})
    
    st.write(response['text'])

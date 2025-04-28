from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os

# Initialize app
app = FastAPI()

# API Key
api_key = os.getenv("OPENAI_API_KEY")

# Input Model
class InterviewRequest(BaseModel):
    experience: str
    designation: str

# Function to generate questions
def generate_interview_questions(experience, designation):
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
    # Create the LLM Chain
    chain = LLMChain(llm=llm, prompt=prompt_template)

    # Run the chain with user inputs
    response = chain.invoke({"experience": experience, "designation": designation})

    return response

# API Route
@app.post("/generate-questions/")
async def generate_questions(request: InterviewRequest):
    questions = generate_interview_questions(request.experience, request.designation)
    return {"questions": questions}
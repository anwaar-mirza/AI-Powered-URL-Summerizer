import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from essentials import *
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['GROQ_API_KEY'] = st.secrets['GROQ_API_KEY']

class YouTubeSummarizer:
    def __init__(self, prompt):
        llm = ChatGroq(model="llama-3.3-70b-versatile")
        chat_prompt = ChatPromptTemplate.from_template(prompt)
        self.chain = chat_prompt | llm
       

    def get_response(self, input_text):
        response = self.chain.invoke({"input": input_text})
        return response.content
    



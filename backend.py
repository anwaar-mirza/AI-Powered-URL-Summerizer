import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from essentials import *



class YouTubeSummarizer:
    def __init__(self, prompt, key):
        llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=key)
        chat_prompt = ChatPromptTemplate.from_template(prompt)
        self.chain = chat_prompt | llm
       

    def get_response(self, input_text):
        response = self.chain.invoke({"input": input_text})
        return response.content
    



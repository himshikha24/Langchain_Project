from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os

import os
from dotenv import load_dotenv
load_dotenv()

#Langchain_ATracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACKING_V2'] = "true"
os.environ["LNAGCHAIN_PROJECT"] = "Simple Q&A chatbot with Ollama"

prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)

def generate_response(question,api_key,engine,temperature,max_tokens):
    llm = ollama(model=engine)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({'question':question})
    return answer

##SIdebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Open AI API Key:", type="password")

engine = st.sidebar.selectbox("Select the Open AI model", ["mistral"])

#adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=1.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

#Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You: ")

if user_input :
    response= generate_response(user_input, engine, temperature, max_tokens)
    st.write(response)


else:
    st.write("Please provide the user input")

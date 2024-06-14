#LANGCHAIN_API_KEY = "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"
#LANGCHAIN_PROJECT = "mental state analyser"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## env var called

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#creating chatbot

## prompt template 
prompt =ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful mental health assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
) 

##streamlit framework
st.title("Langchain Demo With OpenAi api")
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
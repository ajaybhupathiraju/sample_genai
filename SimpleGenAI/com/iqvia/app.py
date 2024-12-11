import dotenv
import streamlit as st
from langchain_community.llms.openai import OpenAIChat
from dotenv import load_dotenv
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_openai import OpenAI,ChatOpenAI

load_dotenv()
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["GORQ_API_KEY"]=os.getenv("GORQ_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

st.title("Application build with langchain using gpt-3.5")
llm = ChatOpenAI(temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"], model_name='gpt-3.5-turbo')

prompt = ChatPromptTemplate.from_messages([
    ("system","As you are an AI assistant engineer, please answer below user questions. If not able to answer just response I don't know."),
    ("human","{query}")
])

input_text = st.text_input("enter your query")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
   response = chain.invoke({"query":input_text})
   st.write(response)

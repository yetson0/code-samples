import streamlit as st
import pypdf

from llama_index import SimpleDirectoryReader
from llama_index import ServiceContext
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex

# get access to openai via API_KEY from .env file
import openai
from dotenv import load_dotenv
import os

load_dotenv()
print(f'OPENAI_API_KEY = {os.getenv("OPENAI_API_KEY")}')
openai.api_key=os.getenv("OPENAI_API_KEY")


with st.sidebar:
  st.title('Chat with Your Data')
  st.markdown('''
    ## About
    The app is an LLM powered chatbot by:
    - openai llm model
    - llama
    - streamlit
    \n /dev/ 2023 by Wlodo Si.
    ''')

def main():
  st.header('Chat with your data')
  reader = SimpleDirectoryReader(input_dir='./data', recursive=True)
  docs = reader.load_data()
  service_context = ServiceContext.from_defaults(llm=OpenAI(model='gpt-3.5-turbo', temperature=0.5, system_prompt='You are a machine learning engineer and your job is to answer technical questions'))
  index = VectorStoreIndex.from_documents(docs, service_context=service_context)
  query = st.text_input('Ask question about your data')
  if query:
    chat_engine = index.as_chat_engine(chat_mode='condense_question', verbose=True)
    response = chat_engine.chat(query)
    st.write(response.response)

if __name__ == '__main__':
  main()
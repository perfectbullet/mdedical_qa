import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
from langchain_ollama import ChatOllama

st.title("🦜🔗 Quickstart App")


def generate_response(input_text):
    # model = ChatOllama(
    #     model='qwen2.5:14b',
    #     base_url='http://127.0.0.1:11434',
    #     temperature=0,
    # )
    model = ChatOpenAI(model='qwen2.5:14b', temperature=0.1, base_url='http://127.0.0.1:11434/v1', api_key='ollama')
    # model = ChatOpenAI(model='qwen2.5:14b',
    #     base_url='http://127.0.0.1:11434',
    #     temperature=0,API_KEY='ollama'
    #                    )
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    generate_response(text)

import streamlit as st
from langchain_openai import ChatOpenAI
from openai import OpenAI

st.title("观想医疗问答")

# moonshot
# client = OpenAI(
#     api_key="sk-BhazmM2Qz12BXRYejKXMhibmTn2uuBrhOQv6bwcJgNVYBiBB",
#     base_url="https://api.moonshot.cn/v1",
# )

# local qwen2.5
llm = ChatOpenAI(model='qwen2.5:14b', temperature=0.1, base_url='http://127.0.0.1:11434/v1', api_key='ollama')

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "moonshot-v1-8k"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("输入问题"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

import streamlit as st

from utils.langchain_rag_for_st import langchain_chat_stream_pure
from utils.logs import logger


def medical_llm_chatbox():
    logger.info('start medical_llm_chatbox')
    query_params = st.query_params
    logger.info('query_params is {}'.format(query_params))
    # 设定不同的列标题和展示的内容

    with st.container(border=True):
        # last_chat_input = st.session_state["last_chat_input"]
        if prompt := st.chat_input('请输入'):
            st.session_state["last_chat_input"] = prompt
            # Prevent submission if Ollama endpoint is not set
            logger.info('prompt is {}', prompt)
            # Generate llama-index stream with user input

            with st.container(border=True):
                output_placeholder = st.empty()
                with st.chat_message("assistant"):
                    with st.spinner("回答中..."):
                        response = ""
                        for token in langchain_chat_stream_pure(prompt, st):
                            response += token
                            output_placeholder.markdown(response)
            # Add the user input to messages state
            st.session_state["messages"].append({"role": "user", "content": prompt})
            # Add the final response to messages state
            st.session_state["messages"].append({"role": "assistant", "content": response})
            with st.container(border=True):
                for msg in st.session_state["messages"]:
                    # log.info('msg is {}'.format(msg))
                    st.chat_message(msg["role"]).write(msg["content"])
    logger.info('end medical_llm_chatbox')

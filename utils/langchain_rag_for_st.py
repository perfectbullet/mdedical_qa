import json
import os
from typing import Any, Dict, List

import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.callbacks import BaseCallbackHandler
from langchain_ollama import ChatOllama

from rag_document.rng_document import create_langchain_ollama_llm
from utils.logs import logger


def get_langchain_ollama_llm(
        model=None,
        base_url=None,
) -> ChatOllama:
    llm = st.session_state.get('llm')
    if not llm:
        logger.info('create llm, model is {}, base_url is {}', model, base_url)
        llm = create_langchain_ollama_llm(model, base_url)
        st.session_state['llm'] = llm
    return llm



class CustomHandler(BaseCallbackHandler):
    def on_llm_start(
            self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        formatted_prompts = "\n".join(prompts)
        logger.info(f"Prompt:\n{formatted_prompts}")


def langchain_chat_stream_pure(q, st):
    """
    Args:
        q: query
        st: st
    Returns:
        yield steam
    """
    sources = []
    ollama_endpoint = st.session_state["ollama_endpoint"]
    selected_model = st.session_state["selected_model"]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个医生, 根据用户提问回答用户的问题"),
            ("user", "{question}")
        ]
    )
    llm = get_langchain_ollama_llm(base_url=ollama_endpoint, model=selected_model)
    print('llm is {}'.format(llm))
    chain = prompt | llm

    for answer in chain.stream({"question": q}, config={"callbacks": [CustomHandler()]}):

        yield answer.content

    st.session_state["sources"] = sources

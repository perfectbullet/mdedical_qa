import streamlit as st

from config import OLLAMA_BASE_URL
from utils.logs import logger
from utils.util_ollama import get_models, get_embedding_models


def set_initial_state():

    ###########
    # General #
    ###########
    if "last_chat_input" not in st.session_state:
        st.session_state["last_chat_input"] = '请输入'

    if "sidebar_state" not in st.session_state:
        # `initial_sidebar_state` must be `"auto"` or `"expanded"` or `"collapsed"`
        st.session_state["sidebar_state"] = "collapsed"

    if "ollama_endpoint" not in st.session_state:
        st.session_state["ollama_endpoint"] = OLLAMA_BASE_URL

    if "embedding_models" not in st.session_state:
        embedding_models = get_embedding_models()
        logger.info('embedding_models is {}'.format(embedding_models))
        st.session_state["embedding_models"] = get_embedding_models()

    if "ollama_models" not in st.session_state:
        try:
            models = get_models()
            st.session_state["ollama_models"] = models
            logger.info('ollama_models is {}'.format(models))
        except Exception:
            st.session_state["ollama_models"] = []
            pass

    if "selected_model" not in st.session_state:
        try:
            if "qwen2.5:14b" in st.session_state["ollama_models"]:
                st.session_state["selected_model"] = (
                    "qwen2.5:14b"  # Default to qwen2.5:14b on initial load
                )
            # if "medical_QA_2024-12-13-v4:latest" in st.session_state["ollama_models"]:
            #     st.session_state["selected_model"] = (
            #         "medical_QA_2024-12-13-v4:latest"  # Default to qwen2.5:14b on initial load
            #     )
            elif "qwen2.5:14b" in st.session_state["ollama_models"]:
                st.session_state["selected_model"] = (
                    "qwen2.5:14b"
                )
            elif "llama3:8b" in st.session_state["ollama_models"]:
                st.session_state["selected_model"] = (
                    "llama3:8b"  # Default to llama3:8b on initial load
                )
            elif "llama2:7b" in st.session_state["ollama_models"]:
                st.session_state["selected_model"] = (
                    "llama2:7b"  # Default to llama2:7b on initial load
                )
            else:
                st.session_state["selected_model"] = st.session_state["ollama_models"][
                    0
                ]  # If llama2:7b is not present, select the first model available
        except Exception:
            st.session_state["selected_model"] = None
            pass

    if "messages" not in st.session_state:
        st.session_state["messages"] = []


    #####################
    # Advanced Settings #
    #####################
    if "advanced" not in st.session_state:
        st.session_state["advanced"] = False

    if "system_prompt" not in st.session_state:
        sys_prompt = """"""
        st.session_state['system_prompt'] = sys_prompt
        # st.session_state["system_prompt"] = (
        #     "You are a sophisticated virtual assistant designed to assist users in comprehensively understanding and extracting insights from a wide range of documents at their disposal. Your expertise lies in tackling complex inquiries and providing insightful analyses based on the information contained within these documents."
        # )

    if "top_k" not in st.session_state:
        st.session_state["top_k"] = 3


    if "chunk_size" not in st.session_state:
        st.session_state["chunk_size"] = 1024

    if "chunk_overlap" not in st.session_state:
        st.session_state["chunk_overlap"] = 200

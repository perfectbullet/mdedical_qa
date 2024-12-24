import streamlit as st

from medical_components.settings import settings


def set_page_config():
    query_params = st.query_params
    # logger.info('query_params is {}', query_params)
    if query_params.get('sidebar_state', '') == 'collapsed':
        # http://localhost:8503/?sidebar_state=collapsed&help=no-help
        sidebar_state = query_params.get('sidebar_state', '')
    else:
        sidebar_state = st.session_state["sidebar_state"]
    st.set_page_config(
        page_title="观想医疗问答",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state=sidebar_state,
    )

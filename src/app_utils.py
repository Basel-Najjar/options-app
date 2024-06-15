import streamlit as st

def reset_page():
    st.cache_data.clear()
    for key in st.session_state.keys():
        del st.session_state[key]
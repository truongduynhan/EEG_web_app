import streamlit as st
from data_load import load_raw_data

st.set_page_config(
    page_title="Visualize EEG",
    page_icon=":brain:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
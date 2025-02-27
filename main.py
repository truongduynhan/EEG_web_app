import streamlit as st
from data_load import load_raw_data

st.set_page_config(
    page_title="Visualize EEG",
    page_icon=":brain:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title('Visualize EEG data')

fn = 'data/chb01_03.edf'
signals, signal_headers, header = load_raw_data(fn)

# st.write(signals.shape)
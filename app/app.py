import streamlit as st

st.set_page_config(
    page_title="YouTube Comments Analyzer",
    page_icon="📺",
)

st.title("YouTube Comments Analyzer")
st.write("This app performs sentiment analysis on comments of a YouTube Video.")
video_url = st.text_input("Enter YouTube Video URL")
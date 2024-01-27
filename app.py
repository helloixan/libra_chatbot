import streamlit as st
from preprocessing import generate_response


def direct_chat(text, role):
    with st.chat_message(role):
        st.write(text)

prompt = st.chat_input("Ketik sesuatu")
if prompt :
    direct_chat(prompt, role="user")
    response = generate_response(prompt)
    direct_chat(response, role="assistant")
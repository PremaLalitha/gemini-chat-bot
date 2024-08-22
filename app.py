import streamlit as st
import google.generativeai as genai #pip install google-generativeai


st.title("Welcome to Infobot")

genai.configure(api_key="AIzaSyD0AJ42-kPJkv_dueFv8wS2xoXpOvnOtmU")

text = st.text_input("Enter Your Question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])



if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)

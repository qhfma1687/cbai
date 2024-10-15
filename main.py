import streamlit as st
from transformers import pipeline

# 챗봇 모델 로드
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Streamlit 앱 설정
st.title("챗봇")
st.write("여기에 질문을 입력하세요:")

# 사용자 입력 받기
user_input = st.text_input("나: ")

if user_input:
    response = chatbot(user_input)
    st.write("챗봇: ", response[0]['generated_text'])

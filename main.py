import streamlit as st
from transformers import pipeline

try:
    chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

    st.title("챗봇")
    st.write("여기에 질문을 입력하세요:")

    user_input = st.text_input("나: ")

    if user_input:
        response = chatbot(user_input, max_length=100, num_return_sequences=1)
        st.write("챗봇: ", response[0]['generated_text'])

except KeyError as e:
    st.error("챗봇 모델 로드 중 오류가 발생했습니다: " + str(e))
except Exception as e:
    st.error("예상치 못한 오류가 발생했습니다: " + str(e))

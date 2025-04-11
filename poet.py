from dotenv import load_dotenv
import getpass
import os
import streamlit as st
import time

load_dotenv(override=True) 

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

import streamlit as st

st.title("poet.py")
content = st.text_input("시의 주제를 제세해주세요!")

if st.button("시 작성 요청하기"):
    with st.spinner("시 작성 중"):
        result = chat_model.predict(content + "에 대해 시를 써줘")
        st.write(result)


#st.write("시")
# print(result)





import os 
import streamlit as st
from langchain_deepseek import ChatDeepSeek


class DeepSeekLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input=user_controls_input

    def get_llm_model(self):
        try:
            deepseek_api_key=self.user_controls_input["DEEPSEEK_API_KEY"]
            selected_deepseek_model=self.user_controls_input["selected_deepseek_model"]
            if deepseek_api_key=='' and os.environ["DEEPSEEK_API_KEY"]=='':
                st.error("please enter the deepseek api key")
            llm=ChatDeepseek(api_key=deepseek_api_key, model=selected_deepseek_model)
        except Exception as e:
            raise ValueError(f"Error occured with exception{e}")
        return llm 
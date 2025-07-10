import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamli_ui(self): 
        st.set_page_config(page_title= self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:
            # get options from config 
            llm_options=self.config.get_llm_options()
            usecases_options= self.config.get_usecase_options()
            # LLM selection
            self.user_controls["select_llm"]= st.selectbox("Select LLM", llm_options)

            if self.user_controls["select_llm"] == "Groq":

                model_options= self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"]= st.selectbox("Select Model", model_options)

                self.user_controls["GROQ_API_KEY"]= st.session_state["GROQ_API_KEY"]=st.text_input("API key", type="password")

                # validate API key

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("please enter your QROQ API KEY to processd. if you do not have one create one ")


                ## usecase sellection
                self.user_controls["selected_usecases"]= st.selectbox("Select_Usecase",usecases_options)
            
            elif self.user_controls["select_llm"] == "OpenAI":

                model_options= self.config.get_openai_model_options()
                self.user_controls["selected_openai_model"]= st.selectbox("Select Model", model_options)

                self.user_controls["OPENAI_API_KEY"]= st.session_state["OPENAI_API_KEY"]=st.text_input("API key", type="password")

                # validate API key

                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning("please enter your OPENAI API KEY to processd. if you do not have one create one ")


                ## usecase sellection
                self.user_controls["selected_usecases"]= st.selectbox("Select_Usecase",usecases_options)

            elif self.user_controls["select_llm"] == "Gemini":

                model_options= self.config.get_gemini_model_options()
                self.user_controls["selected_gemini_model"]= st.selectbox("Select Model", model_options)

                self.user_controls["GEMINI_API_KEY"]= st.session_state["GEMINI_API_KEY"]=st.text_input("API key", type="password")

                # validate API key

                if not self.user_controls["GEMINI_API_KEY"]:
                    st.warning("please enter your GEMINI API KEY to processd. if you do not have one create one ")


                ## usecase sellection
                self.user_controls["selected_usecases"]= st.selectbox("Select_Usecase",usecases_options)

            elif self.user_controls["select_llm"] == "DeepSeek":

                model_options= self.config.get_deepseek_model_options()
                self.user_controls["selected_deepseek_model"]= st.selectbox("Select Model", model_options)

                self.user_controls["DEEPSEEK_API_KEY"]= st.session_state["DEEPSEEK_API_KEY"]=st.text_input("API key", type="password")

                # validate API key

                if not self.user_controls["DEEPSEEK_API_KEY"]:
                    st.warning("please enter your DEEPSEEK API KEY to processd. if you do not have one create one ")


                ## usecase sellection
                self.user_controls["selected_usecases"]= st.selectbox("Select_Usecase",usecases_options)

            return self.user_controls

        


    
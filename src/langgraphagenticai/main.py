import streamlit as st 
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.LLMs.openaillm import OpenAILLM
from src.langgraphagenticai.LLMs.geminillm import GeminiLLM
from src.langgraphagenticai.LLMs.deepseekllm import DeepSeekLLM
from src.langgraphagenticai.graph.graph_builer import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    loads and runs langgraph AgenticAI application with streamlit UI
    this function initializes the UI, handles user input, configure the LLM model
    sets up the graph based on the selected use case, ans display the outputs while 
    implementing exception handling for robustness


    """

    ## load ui
    ui= LoadStreamlitUI()
    user_input = ui.load_streamli_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    user_message= st.chat_input("enter your messge:")

    if user_message:
        try:
            ## configure the llm
            llm_provider = user_input.get("select_llm")
            if llm_provider == "Groq":
                obj_llm_config=GroqLLM(user_controls_input=user_input)
            elif llm_provider == "OpenAI":
                obj_llm_config=OpenAILLM(user_controls_input=user_input)
            elif llm_provider == "Gemini":
                obj_llm_config=GeminiLLM(user_controls_input=user_input)
            elif llm_provider == "DeepSeek":
                obj_llm_config=DeepSeekLLM(user_controls_input=user_input)
            else:
                st.error("Invalid LLM provider selected.")
                return

            model=obj_llm_config.get_llm_model()
            if not model:
                st.error("Error:LLM model could not be initialized")
                return 
            usecase=user_input.get("selected_usecases")

            if not usecase:
                st.error("Error: no use case seleccted")
                return 
            #graph building
            graph_builder=GraphBuilder(model)

            try:
                graph= graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e: 
                st.error(f"Error: Graph set up failed- {e}")
                return 

        except Exception as e:

             st.error(f"Error: Graph set up failed- {e}")
             return 
      

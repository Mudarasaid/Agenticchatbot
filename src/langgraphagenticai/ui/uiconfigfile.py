from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"): 
        self.config= ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFUALT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFUALT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFUALT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_openai_model_options(self):
        return self.config["DEFUALT"].get("OPENAI_MODEL_OPTIONS").split(", ")

    def get_gemini_model_options(self):
        return self.config["DEFUALT"].get("GEMINI_MODEL_OPTIONS").split(", ")

    def get_deepseek_model_options(self):
        return self.config["DEFUALT"].get("DEEPSEEK_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFUALT"].get("PAGE_TITLE")
from src.langgraphagenticai.state.state import State



class BasicChatbotNode:
    """
    this chatboat login implemenation
    """
    def __init__(self,model):
        self.llm= model

    def process(self, state:State)->dict:
        """
        process the input state and generates a chat response
        """
        return {"messages":self.llm.invoke(state['messages'])}
    

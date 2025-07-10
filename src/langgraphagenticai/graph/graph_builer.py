from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder= StateGraph(State)

    def basic_chatboat_build_graph(self):
        """
        buils a basic chatboat using langgraph
        """

        self.basic_chatboat_node= BasicChatbotNode(self.llm)


        self.graph_builder.add_node("chatboat", self.basic_chatboat_node.process)
        self.graph_builder.add_edge(START, "chatboat")
        self.graph_builder.add_edge("chatboat",END)

    def setup_graph(self,usecse:str):
        """
        sets up the graph for the selected use case
        """
        if usecse== "Basic Chatbot":
            self.basic_chatboat_build_graph()
            return self.graph_builder.compile()
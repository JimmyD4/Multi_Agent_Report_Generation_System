import os
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI


# LLM configurations
model = os.getenv("RESEARCH_AGENT_LLM")

llm = ChatOpenAI(
    model=model,
    api_key=os.getenv("OPENAI_API_KEY")
)

researcher_agent = Agent(
    role="Research_Assistant",
    goal="To gather comprehensive, accurate, and diverse information on a given topic, " \
    "synthesizing findings into clear, structured research notes.",
    backstory= (
        "You are an expert in information retrieval and synthesis. "
        "Your goal is to provide the most relevant and critical data points "
        "that will form the backbone of a detailed report. "
        "You are meticulous, resourceful, and always aim for primary sources when possible. "
        "You understand that the quality of the report hinges on the depth and accuracy of your research."),
    llm=llm,
    tools=[SerperDevTool()],
    verbose=True, 
)

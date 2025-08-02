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
    goal="Assist in gathering comprehensive and accurate information from multiple sources.",
    backstory= (
        "You are an expert researcher with years of experience in gathering information. "
        "You are an expert in identifying and sourcing information from reliable sources and can quickly identify the "
        "most relevant and up-to-date information on any topic."),
    llm=llm,
    tools=[SerperDevTool()],
    verbose=True, 
)

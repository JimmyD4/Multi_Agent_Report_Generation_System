
import os
from crewai import Agent
from crewai_tools import FileWriterTool
from langchain_openai import ChatOpenAI

# LLM configurations
model = os.getenv("WRITER_AGENT_LLM")

llm = ChatOpenAI(
    model=model,
    api_key=os.getenv("OPENAI_API_KEY")
)

writer_agent = Agent(
    role="Report_Writer",
    goal="Assist in writing detailed and structured reports based on provided research data.",
    backstory=(
        "You are an experienced report writer with a knack for organizing information into clear and concise reports. "
        "You excel at synthesizing complex information into understandable formats and ensuring that reports are well-structured."),
    llm=llm,
    tools=[FileWriterTool()],
    verbose=True,
)
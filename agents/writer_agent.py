
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
    goal="To compose a detailed, well-structured, and coherent report based on provided research data, " \
    "ensuring clarity, accuracy, and engaging prose.",
    backstory=(
        "You are a skilled writer with a talent for transforming complex information into accessible "
        "and impactful reports. You understand the importance of logical flow, precise language, and "
        "tailoring the content to a professional audience. Your mission is to take raw research and "
        "craft a compelling narrative that effectively communicates key insights."),
    llm=llm,
    #tools=[FileWriterTool()],
    verbose=True,
)
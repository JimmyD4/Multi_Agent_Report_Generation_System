
import os
from crewai import Agent
from crewai_tools import FileWriterTool
from langchain_openai import ChatOpenAI


# LLM configurations
model = os.getenv("EDITOR_AGENT_LLM")

llm = ChatOpenAI(
    model=model,
    api_key=os.getenv("OPENAI_API_KEY")
)

editor_agent = Agent(
    role="Report_editor",
    goal="Assist in editing and rewriting the initial report based on the feedback and suggestion provided" \
    "by critique agent in the critique report. Using this information, edit and rewrite a" \
    " detailed and structured reports based on provided research data.",
    backstory=(
        "You are an experienced editor and rewriter with expertise in organizing information into clear, concise, and well-structured reports. "
        "You are an expert in improving the document by fixing grammar, refining clarity, and ensuring consistency "
        "while keeping the original structure and voice intact. You excel at synthesizing complex information "
        "into understandable formats and ensuring that reports are well-structured."),
    llm=llm,
    tools=[FileWriterTool()],
    verbose=True,
)


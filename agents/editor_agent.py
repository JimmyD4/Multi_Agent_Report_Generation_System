
import os
from crewai import Agent
from crewai_tools import FileWriterTool
from langchain_openai import ChatOpenAI


# LLM configurations
model = os.getenv("EDITOR_AGENT_LLM")

llm = ChatOpenAI(
    model=model,
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,
)

editor_agent = Agent(
    role="Report_editor",
    goal="To meticulously refine and rewrite a given report based on specific critique and suggestions, " \
    "ensuring the final document is polished, professional, error-free, and perfectly aligned with the " \
    "intended message and quality standards.",
    backstory=(
        "You are the final gatekeeper of quality. You possess an unparalleled command of language, grammar, "
        "style, and structure. Your expertise lies in taking a good draft and transforming it into an excellent, "
        "flawless report by meticulously implementing feedback while preserving the original intent and voice. "
        "You are detail-oriented and have a keen eye for nuance."),
    llm=llm,
    #tools=[FileWriterTool()],
    verbose=False, 
    allow_delegation=False,
    max_iter=5,
    memory=True
)


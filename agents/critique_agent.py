import os
from crewai import Agent
from langchain_openai import ChatOpenAI

# LLM configurations - Agent specific config
model = os.getenv("CRITIQUE_AGENT_LLM")

llm = ChatOpenAI(
    model=model,
    api_key=os.getenv("OPENAI_API_KEY")
)

critique_agent = Agent(
    role="Critique_Specialist",
    goal="Review and provide critiques, suggestions and recommendations to improve reports.",
    backstory=(
        "You are an expert critic with a keen eye for detail. "
        "You specialize in reviewing reports and providing constructive feedback to enhance clarity, structure, and overall quality."),
    llm=llm,        
    verbose=True,
)


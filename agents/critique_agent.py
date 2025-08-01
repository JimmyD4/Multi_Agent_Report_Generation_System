import os
from crewai import Agent, LLM

# LLM configurations - Agent specific config
model = os.getenv("CRITIQUE_AGENT_LLM")
temperature = float(os.getenv("CRITIQUE_AGENT_TEMPERATURE"))

llm = LLM(
    model=model,
    temperature=temperature,
    api_key=os.getenv("GOOGLE_API_KEY")
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


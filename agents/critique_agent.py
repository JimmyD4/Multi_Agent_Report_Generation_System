import os
from crewai import Agent
from langchain_openai import ChatOpenAI

# LLM configurations - Agent specific config
model = os.getenv("CRITIQUE_AGENT_LLM")

llm = ChatOpenAI(
    model=model,
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,
)

critique_agent = Agent(
    role="Critique_Specialist",
    goal="To provide a comprehensive, constructive, and actionable critique of a given report, " \
    "identifying strengths, weaknesses, and offering concrete suggestions for improvement in content, " \
    "structure, and overall impact.",
    backstory=(
        "You possess a sharp analytical mind and an unparalleled eye for detail. "
        "You excel at identifying logical fallacies, inconsistencies, content gaps, and structural issues. "
        "Your purpose is not just to point out flaws, but to guide the 'editor' agent towards producing "
        "an exceptional final document. You think strategically about how a report can be made more persuasive, "
        "informative, and professional."),
    llm=llm,
    verbose=False,
    allow_delegation=False,
    max_iter=5,
    memory=True,
)


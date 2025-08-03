from crewai import Process, Crew
import logging

# Configure logging for clean output
logging.getLogger("crewai").setLevel(logging.ERROR)
logging.getLogger("langchain").setLevel(logging.ERROR)

from agents.research_agent import researcher_agent
from agents.writer_agent import writer_agent
from agents.critique_agent import critique_agent
from agents.editor_agent import editor_agent

from tasks.research_agent_task import research_agent_task
from tasks.writer_agent_task import writing_agent_task
from tasks.critique_agent_task import critique_agent_task
from tasks.editor_agent_task import editor_agent_task

research_crewai = Crew(
    agents=[
        researcher_agent,
        writer_agent,
        critique_agent,
        editor_agent,  
    ],
    tasks=[
        research_agent_task,
        writing_agent_task,
        critique_agent_task,
        editor_agent_task,
    ], 
    process=Process.sequential,     
    verbose=False,
    memory=False,
    max_rpm=10,
    share_crew=False,
)
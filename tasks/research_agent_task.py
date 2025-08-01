import textwrap

from crewai import Task
from agents.research_agent import researcher_agent

research_agent_task = Task(
    agent=researcher_agent,
    description=textwrap.dedent("""
                Conduct comprehensive research on the topic: {topic}

                Your tasks:
                1. Search for the most current and relevant information
                2. Gather data from multiple reliable sources
                3. Organize findings in a structured format
                4. Ensure information is accurate and up-to-date

                Provide a detailed research summary with:
                - Key findings
                - Expert opinions
                - Recent developments
                - Reliable sources used
                """),
    expected_output="A detailed research summary with key findings, expert opinions, conclusion, and reliable sources used.",
    output_file="reports/research_summary.txt",
)
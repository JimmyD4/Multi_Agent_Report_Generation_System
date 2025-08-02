import textwrap

from crewai import Task
from agents.critique_agent import critique_agent
from tasks.writer_agent_task import writing_agent_task
from tasks.research_agent_task import research_agent_task

critique_agent_task = Task(
    agent=critique_agent,
    description=textwrap.dedent("""
                Review and critique the first draft report written by the writer agent.

                Your tasks is to critique the report based on the following criteria:
                1. Analyze the structure and clarity of the report
                2. Provide constructive feedback on content, organization, and presentation
                3. Suggest improvements to enhance the report's quality
                4. Ensure the critique is detailed and actionable
                5. Highlight strengths and areas for improvement
                6. Maintain a professional and objective tone in your critique
                7. Check if the report follows APA citation format for in-text citations and references

                Provide a detailed critique with:
                    - Strengths of the report
                    - Areas for improvement
                    - Specific suggestions for enhancement
                    - Overall assessment of the report's quality
                """),
    expected_output="A detailed critique with strengths, areas for improvement, specific suggestions, and overall assessment of the report's quality.",
    context=[writing_agent_task, research_agent_task],
    output_file="reports/critique_report.txt",
)
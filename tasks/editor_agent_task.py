import textwrap

from crewai import Task
from agents.editor_agent import editor_agent
from tasks.research_agent_task import research_agent_task
from tasks.critique_agent_task import critique_agent_task
from tasks.writer_agent_task import writing_agent_task

editor_agent_task = Task(
    agent=editor_agent,
    description=textwrap.dedent("""
                After the writer agent has written the initial report and forwarded it to the critique agent, the critique agent
                has given feedback on the initial report. Your goal is to revise and improve the report based on the critique provided.

                Your tasks:
                1. Carefully review the critique and suggestions.
                2. Incorporate the feedback to enhance clarity, structure, content, and overall quality of the report.
                3. Ensure all suggestions are addressed comprehensively.
                4. Maintain APA citation format for any new or existing in-text citations and provide a full reference list at the end of the report.

                Provide the improved, well-structured report with standard best practices in technical writing.
                """),
    expected_output="An improved and revised report based on the provided critique.",
    context=[research_agent_task, writing_agent_task, critique_agent_task],
    output_file="reports/final_improved_report.txt",
)
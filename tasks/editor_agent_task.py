import textwrap

from crewai import Task
from agents.editor_agent import editor_agent
from tasks.critique_agent_task import critique_agent_task
from tasks.writer_agent_task import writing_agent_task

editor_agent_task = Task(
    agent=editor_agent,
    description=textwrap.dedent("""
                Your goal is to revise and improve the initial report based on the critique provided.

                Your tasks:
                1.  Understand Critique: Thoroughly read and internalize the critique report provided by the critique agent. Prioritize the recommendations.
                2.  Strategic Revision: Systematically go through the initial report, applying all relevant feedback. This includes:
                    *   Rewriting sections for clarity, conciseness, and impact.
                    *   Adding missing information or expanding on underdeveloped points as suggested.
                    *   Restructuring paragraphs or sections for better logical flow.
                    *   Addressing any identified biases or inconsistencies.
                3.  Grammar, Spelling & Punctuation: Conduct a comprehensive proofread to eliminate all grammatical errors, spelling mistakes, and punctuation issues.
                4.  Style & Tone Consistency: Ensure the report maintains a consistent, professional, and appropriate style and tone throughout.
                5.  Fact-Checking & Cross-Referencing: While not a primary research task, perform quick checks for obvious factual discrepancies or misinterpretations if highlighted in the critique.
                6.  Overall Polish: Ensure the report is perfectly formatted, easy to read, and ready for final presentation. The goal is a report that is superior to the initial draft in every measurable way.
                7.  Maintain APA Citation Format: Ensure all in-text citations and the reference list at the end of the report adhere to APA format.
                """),
    expected_output="The complete, revised, and polished final version of the report",
    context=[writing_agent_task, critique_agent_task],
    output_file="reports/final_report.txt",
)
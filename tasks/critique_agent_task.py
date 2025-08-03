import textwrap

from crewai import Task
from agents.critique_agent import critique_agent
from tasks.writer_agent_task import writing_agent_task
from tasks.research_agent_task import research_agent_task

critique_agent_task = Task(
    agent=critique_agent,
    description=textwrap.dedent("""

                Your tasks is to critique the initial report based on the following criteria:
                1.  Holistic Review: Read the entire report carefully, assessing its overall purpose, target audience, and effectiveness.
                2.  Content Analysis:
                     -  Accuracy & Completeness: Verify factual accuracy (where possible/implied by context) and identify any missing information or unsupported claims.
                     -  Clarity & Conciseness: Evaluate if the language is clear, unambiguous, and avoids jargon. Is it concise without losing meaning?
                     -  Argument & Evidence: Assess if arguments are well-supported by evidence and if conclusions logically follow from the data.
                     -  Bias Check: Identify any potential biases in presentation or interpretation.
                3.  Structure & Flow Analysis:
                     -  Logical Organization: Is the report logically structured? Are sections ordered effectively?
                     -  Transitions: Do ideas flow smoothly between paragraphs and sections?
                     -  Readability: Is it easy to read and digest? Are headings and subheadings effective?
                4.  Impact & Engagement:
                     -  Engagement: Does the report hold the reader's attention?
                     -  Persuasiveness:** If applicable, is the report persuasive and impactful?
                5.  Constructive Feedback Generation: For each identified area for improvement, provide specific, actionable recommendations. Frame feedback constructively.
                6.  Prioritization: Categorize feedback by criticality (e.g., Major, Moderate, Minor) or by section of the report.
                7.  Formatting & Style Check: Ensure the report adheres to any specified formatting guidelines (e.g., APA style) and maintains a consistent tone and style.
                """),
    expected_output="A Critique Report in markdown, structured as follows:"
                    "Executive Summary of Critique: Overall assessment."
                    "Strengths of the Report:"
                    " - Areas for Improvement & Recommendations:**"
                    "  [Section/Aspect]: [Specific issue] -> [Actionable Recommendation]"
                    "  ... (List multiple points as needed)"
                    "  General Comments/Further Suggestions:",
    context=[writing_agent_task, research_agent_task],
    output_file="reports/report_critique.txt",
)
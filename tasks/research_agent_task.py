import textwrap

from crewai import Task
from agents.research_agent import researcher_agent

research_agent_task = Task(
    agent=researcher_agent,
    description=textwrap.dedent("""
                Conduct comprehensive research on the topic: {topic}

                Your tasks:
                1. Understand Research Objective: Clearly identify the core questions or areas of focus provided by the user or the overall task.
                2. Source Identification: Identify a diverse range of credible sources (e.g., academic papers, reputable news outlets, official reports, industry analyses, expert opinions). Prioritize primary sources.
                3. Data Extraction & Synthesis: Efficiently extract key facts, figures, trends, and perspectives. Synthesize this information, identifying common themes, discrepancies, and critical insights.
                4. Structured Output: Present your findings in a structured, easy-to-digest format. This should include:
                    * Key Findings Summary: A concise overview of the most important discoveries.
                    * Detailed Notes: Organized by sub-topic, clearly citing sources where appropriate.
                    * Potential Gaps/Further Questions: Highlight any areas where information was scarce or conflicting, or where further investigation might be beneficial.
                    * Source List: A comprehensive list of all consulted sources.
                5. Quality Assurance: Ensure all information is factually accurate and unbiased.
                """),
    expected_output="A markdown document containing the Key Findings Summary, Detailed Notes, Potential Gaps/Further Questions, and Source List.",
    output_file="reports/research_summary.txt",
    verbose=False,
)
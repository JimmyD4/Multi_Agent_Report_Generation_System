import textwrap

from crewai import Task
from agents.writer_agent import writer_agent
from tasks.research_agent_task import research_agent_task

writing_agent_task = Task(
    agent=writer_agent,
    description=textwrap.dedent("""
                Write a comprehensive report based on the topic provided and the research summary provided by the research agent.
                
                Your tasks:
                    1.  Review Research Data: Thoroughly read and understand all research notes and data provided by the "Research" agent. Identify the main themes, arguments, and supporting evidence.
                    2.  Outline Report Structure: Develop a logical and comprehensive outline for the report, including an introduction, main sections (aligned with research themes), and a conclusion. Consider standard report conventions (e.g., executive summary, methodology if applicable).
                    3.  Draft Initial Sections: Write clear, concise, and informative prose for each section, integrating the research data seamlessly.
                    4.  Data Integration: Ensure all relevant facts, figures, and findings are accurately incorporated and properly attributed within the text.
                    5.  Maintain Cohesion & Flow: Focus on smooth transitions between paragraphs and sections, ensuring the report reads as a unified and coherent document.
                    6.  Adhere to Tone & Style: Maintain a professional, objective, and analytical tone suitable for a formal report.
                    7.  Preliminary Review: Conduct a basic self-review for clarity, completeness, and initial grammar/spelling errors.
                    8.  Cite Sources: Ensure all sources used in the report are cited in APA format, both as in-text citations and in a reference section at the end.
                """),
    expected_output="A markdown document representing the complete first draft of the report, structured with headings and subheadings.",
    context=[research_agent_task],
    output_file="reports/initial_report.txt",
)

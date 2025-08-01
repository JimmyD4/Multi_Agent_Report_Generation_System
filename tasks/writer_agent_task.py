import textwrap

from crewai import Task
from agents.writer_agent import writer_agent
from tasks.research_agent_task import research_agent_task

writing_agent_task = Task(
    agent=writer_agent,
    description=textwrap.dedent("""
                Write a comprehensive report based on the provided on the topic and the research findings 
                from the research agent report.
                
                Your tasks:
                1. Analyze the research data provided
                2. Structure the report into clear sections
                3. Include an executive summary, main content, findings, and conclusion
                4. Ensure the report is well-organized and easy to understand
                5. cite all sources used in the report in APA format as intext citation and in the reference section
                
                Provide a well-structured report with:
                - Executive summary
                - Main content with detailed analysis
                - Main Findings
                - Recommendations and conclusions
                - References in APA format
                """),
    expected_output="A well-structured report with an executive summary, main content, findings, and conclusions, along with references in APA format.",
    context=[research_agent_task],
    output_file="reports/first_draft_report.txt",
)

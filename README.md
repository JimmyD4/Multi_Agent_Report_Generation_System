# 🚀 AI-Powered Multi-Agent Report Generation System

This project showcases a  AI system built with [CrewAI](https://www.crewai.com/), designed to automate the end-to-end process of research, report writing, critiquing, and final editing. It leverages a team of specialized AI agents working collaboratively to produce high-quality, well-structured reports, significantly streamlining the report generation workflow.

## ✨ Features

*   **Comprehensive Research:** An AI Research Assistant gathers up-to-date and accurate information from multiple online sources using the Serper Dev tool.
*   **Structured Report Writing:** An AI Report Writer synthesizes research data into an initial draft, following a predefined structure and adhering to APA citation guidelines.
*   **Intelligent Report Critiquing:** An AI Critique Specialist reviews the initial report, providing detailed feedback, suggestions for improvement, and an overall quality assessment.
*   **Adaptive Report Editing:** An AI Report Editor revises and polishes the report based on the critique, ensuring clarity, consistency, and adherence to best practices in technical writing.
*   **Sequential Agent Workflow:** Agents operate in a carefully orchestrated sequence, passing outputs from one stage to the next for iterative refinement.
*   **OpenAI LLM Integration:** Utilizes OpenAI models for powerful language generation and understanding.
*   **Streamlit Web Interface:** Provides an intuitive web application for easy interaction and viewing of results.

## Architecture - How It Works

The system operates as a multi-agent AI crew, where each agent specializes in a distinct phase of report generation. The process is sequential, ensuring that each step builds upon the previous one.

1.  **🔍 Research Agent (Research Assistant)**
    *   **Role:** Gathers comprehensive and accurate information.
    *   **Tool:** `SerperDevTool` (for web searches).
    *   **Task:** Conducts in-depth research on the given topic, collecting key findings, expert opinions, and recent developments.
    *   **Output:** `reports/research_summary.txt` (Detailed research summary).

2.  **✍️ Writer Agent (Report Writer)**
    *   **Role:** Drafts detailed and structured reports.
    *   **Task:** Analyzes the research summary and writes a comprehensive initial report, including an executive summary, main content, findings, recommendations, conclusions, and APA-formatted references.
    *   **Output:** `reports/initial_report.txt` (First draft of the report).

3.  **📊 Critique Agent (Critique Specialist)**
    *   **Role:** Reviews and provides constructive feedback.
    *   **Tool:** No external tool; uses its LLM capabilities for analysis.
    *   **Task:** Critiques the initial report based on structure, clarity, content, organization, presentation, and APA citation adherence. Provides strengths, areas for improvement, and specific suggestions.
    *   **Output:** `reports/report_critique.txt` (Detailed critique report).

4.  **📝 Editor & Finalizer Agent (Report Editor and Writer)**
    *   **Role:** Edits and finalizes the report.
    *   **Task:** Revises and improves the initial report by incorporating all feedback and suggestions from the Critique Agent, ensuring a polished, well-structured, and consistent final document.
    *   **Output:** `reports/final_report.txt` (The complete, finalized report).

The entire process is orchestrated by a CrewAI `Crew` with a `sequential` process, ensuring a logical flow from research to final output.

## 🛠️ Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

*   Python 3.9+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/your_repo_name.git
    cd your_repo_name
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv myenv
    source myenv/bin/activate  
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### API Keys & Configuration

This project requires API keys for OpenAI (for LLMs) and SerperDev (for web search).

1.  **Obtain API Keys:**
    *   **OpenAI:** Get your API key from [OpenAI AI Studio]
    *   **SerperDev:** Get your API key from [SerperDev](https://serper.dev/).

2.  **Create a `.env` file:**
    In the root directory of your project, create a file named `.env` and add your API keys and LLM configurations like this:


### `requirements.txt` Content

Create a file named `requirements.txt` in your project root with the following content:



## Project Structure

├── agents/
│   ├── __init__.py
│   ├── critique_agent.py
│   ├── editor_agent.py
│   ├── research_agent.py
│   └── writer_agent.py


├── tasks/
│   ├── __init__.py
│   ├── critique_agent_task.py
│   ├── editor_agent_task.py
│   ├── research_agent_task.py
│   └── writer_agent_task.py


├── reports/                
├── .env.example             
├── .env                    
├── app.py                  
├── crew.py                  
├── main.py                  
└── requirements.txt         


### Output Files
All generated reports will be saved in the reports/ directory:


### Author

Jigme Dorji
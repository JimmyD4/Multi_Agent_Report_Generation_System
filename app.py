import streamlit as st
import os
import time
from dotenv import load_dotenv

load_dotenv()

from crew import research_crewai

def check_api_keys():
    """Check if required API keys are set"""
    required_vars = ['SERPER_API_KEY', "OPENAI_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    return missing_vars


def main():
    """Main Streamlit app"""
    st.set_page_config(
        page_title="Multi-Agent Report Generator",
        page_icon="🔬",
        layout="wide"
    )

    st.title("AI-Powered Multi-Agent Report Generation System")
    st.markdown("*Powered by CrewAI Multi-Agent System*")
    st.markdown("*AI system built with CrewAI, designed to automate the " \
    "end-to-end process of research, report writing, critiquing, and final editing. " \
    "It leverages a team of specialized AI agents working collaboratively to produce high-quality, " \
    "well-structured reports, significantly streamlining the report generation workflow.*")

    os.makedirs('reports', exist_ok=True)

    # Initialize session state
    if 'research_completed' not in st.session_state:
        st.session_state.research_completed = False
    if 'research_result' not in st.session_state:
        st.session_state.research_result = None
    if 'research_error' not in st.session_state:
        st.session_state.research_error = None

    # Sidebar for API key status
    with st.sidebar:
        st.header("⚙️ Configuration")
        missing_vars = check_api_keys()

        if missing_vars:
            st.error("❌ Missing API Keys")
            st.write("Please set the following environment variables:")
            for var in missing_vars:
                st.code(f"{var}=your_api_key_here")
            st.info("💡 Create a .env file in the project root with your API keys")
        else:
            st.success("✅ API Keys Configured")

        st.header("🤖 Multi-Agent System")
        st.markdown("""
        **Multi-Agents:**
        - 🔍 **Research Expert**: Gathers information
        - ✍️ **Writer**: Writes detailed reports
        - 📊 **Critique/Reviewer**: Reviews and critiques reports
        - 📝 **Editor**: Edits and finalizes reports
        """)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with st.container():
        st.markdown("### 📝 Research Topic")
        topic = st.text_area(
        "Enter your topic:",
        height=250,
        placeholder="Write a detailed research question here...",
        help="Be specific to get better results."
    )

        if st.button("🚀 Start Generating", type="primary", disabled=bool(missing_vars)):
            if not topic.strip():
                st.error("Please enter a topic.") 
            else:
                st.session_state.research_completed = False
                st.session_state.research_result = None
                st.session_state.research_error = None

                # Show progress
                progress_container = st.container()
                status_container = st.container()

                with progress_container:
                    st.info("🔄 Work in progress...")
                    progress_bar = st.progress(0)

                    for i in range(25):
                        progress_bar.progress(i)
                        time.sleep(0.05)

                with status_container:
                    st.write("🔍 Multi agents are working...")
                    st.write("📊 Analyzing data...")
                    st.write("✍️ Writing report...")
                    st.write("📊 Critiquing report...")
                    st.write("📝 Editing final report...")

                progress_bar.progress(50)

                # Run research
                try:
                    result = research_crewai.kickoff({"topic": topic})
                    st.session_state.research_result = result
                    st.session_state.research_completed = True
                    st.session_state.research_error = None
                    progress_bar.progress(100)
                except Exception as e:
                    st.session_state.research_error = str(e)
                    st.session_state.research_completed = True
                    progress_bar.progress(100)

                progress_container.empty()
                status_container.empty()
                st.rerun()


    with col2:
        with st.container():
            st.markdown("#### 📊 Status")
            status_text = ""
            if st.session_state.research_completed:
                if st.session_state.research_error:
                    status_text = f"❌ {st.session_state.research_error}"
                    st.markdown(f"<div style='color:red; font-size: 0.9em;'>{status_text}</div>", unsafe_allow_html=True)
                else:
                    status_text = "✅ Completed!"
                    st.markdown(f"<div style='color:green; font-size: 0.9em;'>{status_text}</div>", unsafe_allow_html=True)
            else:
                status_text = "⏳ Waiting for research topic..."
                st.markdown(f"<div style='color:gray; font-size: 0.85em;'>{status_text}</div>", unsafe_allow_html=True)


    # Results section
    if st.session_state.research_completed and not st.session_state.research_error:
        st.header("📄 Results")

        output_files = {
            "reports/research_summary.txt": "🔍 Research Summary",
            "reports/first_draft_report.txt": "📝 Draft Report",
            "reports/critique_report.txt": "📊 Critique Report",
            "reports/final_improved_report.txt": "📝 Final Report",
            "__direct_crewai_output__": "✨ CrewAI Final Result"
        }

        tabs = st.tabs(list(output_files.values()))

        for i, (filename, title) in enumerate(output_files.items()):
            with tabs[i]:
                if filename == "__direct_crewai_output__":
                    if st.session_state.research_result:
                        st.subheader("Raw CrewAI Output")
                        crew_output_string = str(st.session_state.research_result)
                        st.markdown(crew_output_string)
                        
                        st.download_button(
                            label="📥 Download CrewAI Final Result",
                            data=crew_output_string,
                            file_name="crewai_final_result.md",
                            mime="text/markdown"
                        )
                    else:
                        st.info("CrewAI direct output not available.")
                elif os.path.exists(filename):
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    st.markdown(content)

                    # Download button
                    st.download_button(
                        label=f"📥 Download {title}",
                        data=content,
                        file_name=os.path.basename(filename),
                        mime="text/markdown"
                    )
                else:
                    st.warning(f"File '{filename}' not found. It might not have been generated yet.")

    # Footer
    st.markdown("---")
    st.markdown("*Built with CrewAI, Streamlit, and OpenAI*")


if __name__ == "__main__":
    main()
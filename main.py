from dotenv import load_dotenv
from crew import research_crewai
load_dotenv()


def run(topic: str):
    result = research_crewai.kickoff(
        inputs={"topic": topic})
    
    print(result)

if __name__ == "__main__":
    topic = input("Enter the topic for the research report: ")
    run(topic)



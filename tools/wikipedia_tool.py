from langchain.tools import tool
import wikipedia

@tool
def search_wikipedia(query: str) -> str:
    """Search and summarize a topic from Wikipedia"""
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except Exception as e:
        return f"Error fetching Wikipedia summary: {e}" 
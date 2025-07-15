from langchain.tools import tool

@tool
def reverse_text(text: str) -> str:
    """Reverse the input text"""
    return text[::-1]

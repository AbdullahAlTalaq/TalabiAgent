# main.py

from requestPy import create_ticket
from llama_index.agent import Agent  # Replace with correct import if different
from llama_index.llms import Ollama  # Replace with correct import if different

def Send_Request(description: str, subject: str, email: str, priority: int, status: int) -> str:
    """
    Tool: Send_Request

    Description:
        This tool allows an AI agent to send a user support or service request. It packages the 
        necessary information into a request format that can be forwarded to the appropriate system.

    Parameters:
        description (str): A detailed description of the user's request or issue.
        subject (str): A short subject or title for the request.
        email (str): The email address of the user submitting the request.
        priority (int): The priority level of the request (e.g., 1 = High, 2 = Medium, 3 = Low).
        status (int): The status code of the request (e.g., 0 = New, 1 = In Progress, 2 = Resolved).

    Returns:
        str: A confirmation message or ticket ID indicating the request has been successfully submitted.

    Usage:
        Use this tool when a user needs to report an issue, request help, or submit feedback.
    """
    return create_ticket(description, subject, email, priority, status)

Send_agent = Agent( 
    name="Send Request agent", 
    role="Send a request to a specific website",  
    model=Ollama(id="your-model-id"),  # Replace with the actual model ID
    tools=[Send_Request], 
    instructions=[], #write the instrcutions 
    markdown=True,
)

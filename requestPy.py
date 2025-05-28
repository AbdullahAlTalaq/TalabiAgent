# requestPy.py

import requests
from requests.auth import HTTPBasicAuth

# Replace these with your Freshdesk credentials
FRESHDESK_DOMAIN = "yalhabboub"
API_KEY = "2RO4kyCRU5J2o9D79cJ6"

url = f"https://{FRESHDESK_DOMAIN}.freshdesk.com/api/v2/tickets"
headers = {"Content-Type": "application/json"}

def create_ticket(description: str, subject: str, email: str, priority: int, status: int) -> str:
    ticket_data = {
        "description": description,
        "subject": subject,
        "email": email,
        "priority": priority,
        "status": status
    }

    response = requests.post(
        url,
        auth=HTTPBasicAuth(API_KEY, "X"),
        headers=headers,
        json=ticket_data
    )

    if response.status_code == 201:
        ticket_id = response.json().get("id")
        return f"✅ Ticket created successfully! Ticket ID: {ticket_id}"
    else:
        return f"❌ Failed to create ticket. Status Code: {response.status_code}\nResponse: {response.text}"

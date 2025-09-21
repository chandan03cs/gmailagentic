"""
Gemini AI utility functions.
"""
from google import genai

def get_ai_plan(events, emails, api_key):
    """Generate a daily plan using Gemini AI based on events and emails."""
    client = genai.Client(api_key=api_key)
    prompt = f"""
    You are a productivity assistant.\n\nToday's Calendar Events:\n{events}\n\nUnread Important Emails:\n{emails}\n\n1. Summarize meetings for today.\n2. List urgent emails that may need response.\n3. Suggest a prioritized daily task plan.\n"""
    chat = client.chats.create(model="gemini-1.5-pro")
    response = chat.send_message(prompt)
    return response.text

"""
Google Calendar and Gmail utility functions.
"""
import datetime

def get_today_events(calendar_service):
    """Fetch today's events from the user's primary Google Calendar."""
    now = datetime.datetime.now(datetime.UTC)
    start = now.isoformat()
    end = (now + datetime.timedelta(days=1)).isoformat()
    events_result = calendar_service.events().list(
        calendarId="primary",
        timeMin=start,
        timeMax=end,
        singleEvents=True,
        orderBy="startTime"
    ).execute()
    return events_result.get("items", [])

def get_unread_emails(gmail_service):
    """Fetch up to 5 unread emails from the user's Gmail inbox."""
    results = gmail_service.users().messages().list(
        userId="me", labelIds=["UNREAD"], maxResults=5
    ).execute()
    messages = results.get("messages", [])
    emails = []
    for msg in messages:
        msg_data = gmail_service.users().messages().get(userId="me", id=msg["id"]).execute()
        snippet = msg_data.get("snippet", "")
        emails.append(snippet)
    return emails

def schedule_focus_block(calendar_service):
    """Schedule a 2-hour focus block in the user's calendar starting 1 hour from now."""
    now = datetime.datetime.now(datetime.UTC)
    start_time = (now + datetime.timedelta(hours=1)).replace(microsecond=0).isoformat()
    end_time = (now + datetime.timedelta(hours=3)).replace(microsecond=0).isoformat()
    event = {
        "summary": "Focus Work",
        "start": {"dateTime": start_time},
        "end": {"dateTime": end_time},
    }
    event = calendar_service.events().insert(calendarId="primary", body=event).execute()
    return event.get("htmlLink")

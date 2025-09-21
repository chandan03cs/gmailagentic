import streamlit as st
# Import custom modules for modularity
from modules.google_auth import get_services
from modules.google_utils import get_today_events, get_unread_emails, schedule_focus_block
from modules.ai_utils import get_ai_plan

# ----------------------
# CONFIGURATION
# ----------------------
# Set your Gemini API key here or use an environment variable for security
GEMINI_API_KEY = "MY_GEMINI_KEY"

# ----------------------
# STREAMLIT UI
# ----------------------
st.set_page_config(page_title="Agentic AI Daily Assistant", layout="centered")

st.title("🤖 Agentic AI Daily Assistant")
st.write("Get your daily summary of meetings, unread emails, and an AI-generated task plan.")

# Authenticate and fetch data
if st.button("🔑 Connect to Google"):
    # Authenticate and store services in session state
    calendar_service, gmail_service = get_services()
    st.session_state["calendar_service"] = calendar_service
    st.session_state["gmail_service"] = gmail_service
    st.success("✅ Connected to Google APIs")

# Main app logic after authentication
if "calendar_service" in st.session_state and "gmail_service" in st.session_state:
    if st.button("📅 Generate My Daily Plan"):
        # Fetch today's events and unread emails
        events = get_today_events(st.session_state["calendar_service"])
        emails = get_unread_emails(st.session_state["gmail_service"])

        st.subheader("Today's Calendar Events")
        if events:
            for ev in events:
                event_time = ev.get('start', {}).get('dateTime', '') or ev.get('start', {}).get('date', '')
                st.write(f"- {ev.get('summary', 'No Title')} at {event_time}")
        else:
            st.write("No events found.")

        st.subheader("Unread Emails (Snippets)")
        if emails:
            for e in emails:
                st.write(f"- {e}")
        else:
            st.write("No unread important emails.")

        st.subheader("🤖 AI Suggested Daily Plan")
        # Generate AI plan using Gemini
        ai_plan = get_ai_plan(events, emails, GEMINI_API_KEY)
        st.write(ai_plan)

    if st.button("⏱️ Schedule Focus Block"):
        # Schedule a focus block in Google Calendar
        link = schedule_focus_block(st.session_state["calendar_service"])
        st.success(f"✅ Focus block scheduled! [View in Calendar]({link})")

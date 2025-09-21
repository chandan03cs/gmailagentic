# Agentic AI Daily Assistant

A Streamlit app that summarizes your Google Calendar events, unread Gmail messages, and generates a daily plan using Gemini AI.

## Features
- Google OAuth2 authentication
- Fetches today's Google Calendar events
- Fetches up to 5 unread Gmail messages
- Uses Gemini AI to generate a daily plan
- Schedules a focus block in your calendar

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Google Cloud project and download `credentials.json` for OAuth2.
4. Add your Gemini API key in `app.py` or as an environment variable.
5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Project Structure
- `app.py` — Main Streamlit app
- `modules/google_auth.py` — Google authentication and service creation
- `modules/google_utils.py` — Calendar and Gmail utility functions
- `modules/ai_utils.py` — Gemini AI integration
- `requirements.txt` — Python dependencies

## Notes
- You must have access to the Google APIs and Gemini API with sufficient quota.
- This project is for educational/demo purposes.

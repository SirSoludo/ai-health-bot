# AI Health Bot

A lightweight, rule-based health chatbot built with Python and Flask. You describe a symptom, the bot asks follow-up questions one at a time, then suggests possible conditions with reasoning and first-aid tips. Every message is checked for emergency keywords so urgent cases are flagged immediately. Built as an educational final-year project.

## Run

```bash
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. The SQLite database (`health_bot.db`) is created automatically on first run.

## Project files

| Path | What it does |
|---|---|
| `app.py` | Flask routes: home, chat page, tips, referral, and the `/api/chat`, `/api/new-topic`, `/api/clear-history` endpoints |
| `health_bot/engine.py` | Conversation state machine: detects the symptom category, asks follow-ups, scores possible conditions |
| `health_bot/knowledge_base.py` | Symptom categories, follow-up questions, conditions, reasoning and first-aid tips |
| `health_bot/emergency.py` | Keyword-based emergency detector, run on every message |
| `database.py` | SQLite storage for per-session chat history |
| `templates/` | Pages: `base.html` (layout), `index.html`, `chat.html`, `tips.html`, `referral.html` |
| `static/css/style.css`, `static/js/chat.js` | Styling and the chat interface |
| `requirements.txt` | Python dependencies (Flask) |

## Notes

- Change `app.secret_key` in `app.py` before deploying anywhere public.
- This system does not provide medical diagnoses and does not replace professional healthcare advice.

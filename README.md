# AI Health Bot System

A lightweight, rule-based AI Health Bot built with Python (Flask), for educational/final-year project purposes.

## Setup

```
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## How it works

- `health_bot/knowledge_base.py` — symptom categories, follow-up questions, and possible conditions with reasoning and first-aid tips.
- `health_bot/emergency.py` — keyword-based emergency detector, checked on every message.
- `health_bot/engine.py` — conversation state machine: detects the symptom category, asks follow-up questions one at a time, then scores possible conditions based on the answers.
- `database.py` — SQLite storage for per-session chat history.
- `app.py` — Flask routes tying everything together.

## Important

This system does not provide medical diagnoses and does not replace professional healthcare advice.
It is a rule-based educational demonstration only.

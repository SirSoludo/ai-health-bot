import uuid
from flask import Flask, render_template, request, jsonify, session

from database import init_db, save_message, get_history, clear_history
from health_bot.engine import handle_message, clear_session

app = Flask(__name__)
app.secret_key = "university-project-secret-key"

init_db()


def get_session_id():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    return session["session_id"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat")
def chat_page():
    session_id = get_session_id()
    history = get_history(session_id)
    return render_template("chat.html", history=history)


@app.route("/api/chat", methods=["POST"])
def api_chat():
    session_id = get_session_id()
    user_message = request.json.get("message", "").strip()

    if not user_message:
        return jsonify({"type": "error", "message": "Please type something."})

    save_message(session_id, "user", user_message)
    result = handle_message(session_id, user_message)
    bot_reply = format_bot_reply(result)
    save_message(session_id, "bot", bot_reply)

    return jsonify({"reply": bot_reply, "result": result})


@app.route("/api/new-topic", methods=["POST"])
def api_new_topic():
    session_id = get_session_id()
    clear_session(session_id)
    return jsonify({"status": "ok"})


@app.route("/api/clear-history", methods=["POST"])
def api_clear_history():
    session_id = get_session_id()
    clear_history(session_id)
    clear_session(session_id)
    return jsonify({"status": "ok"})


@app.route("/referral")
def referral_page():
    return render_template("referral.html")


@app.route("/tips")
def tips_page():
    return render_template("tips.html")


def format_bot_reply(result: dict) -> str:
    if result["type"] == "emergency":
        return (
            f"This sounds like it could be an emergency. {result['reason']} "
            "Please call your local emergency number or go to the nearest hospital right away. "
            "Visit the Healthcare Referral page for emergency contacts."
        )

    if result["type"] == "question":
        q = result["question"]
        options_text = " / ".join(q["options"])
        if result.get("retry"):
            return (f"Sorry, I didn't catch that. {q['text']} "
                    f"Please reply with one of these options or its number: ({options_text})")
        return f"{q['text']} ({options_text})"

    if result["type"] == "clarify":
        return (
            "I'm not fully sure I understood your concern. Could you describe your main "
            "symptom, for example 'I have a headache' or 'I have a stomach ache'?"
        )

    if result["type"] == "result":
        conditions = result["conditions"]
        if not conditions:
            return (
                "Based on your answers, I couldn't confidently match this to a specific condition. "
                "It's best to consult a healthcare professional for a proper assessment."
            )
        lines = ["Based on what you've shared, here are some possibilities (not a diagnosis):", ""]
        for c in conditions:
            lines.append(f"• {c['name']}")
            lines.append(f"  Why: {c['explanation']}")
            lines.append(f"  First aid / self-care: {c['first_aid']}")
            lines.append("")
        lines.append(
            "This is general guidance only. If symptoms are severe, worsening, or persistent, "
            "please consult a licensed healthcare professional."
        )
        return "\n".join(lines)

    return "Sorry, something went wrong. Could you rephrase that?"


if __name__ == "__main__":
    app.run(debug=True)

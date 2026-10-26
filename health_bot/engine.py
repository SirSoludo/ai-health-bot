"""
Rule-based conversation engine for the AI Health Bot.
One SessionState instance is kept per browser session (in memory).
"""

from health_bot.knowledge_base import SYMPTOM_CATEGORIES, MATCH_THRESHOLD
from health_bot.emergency import check_emergency

_sessions = {}


class SessionState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.category = None
        self.questions = []
        self.question_index = 0
        self.answers = {}


def get_session(session_id: str) -> SessionState:
    if session_id not in _sessions:
        _sessions[session_id] = SessionState()
    return _sessions[session_id]


def clear_session(session_id: str):
    _sessions.pop(session_id, None)


def _detect_category(text: str):
    lowered = text.lower()
    for name, data in SYMPTOM_CATEGORIES.items():
        for keyword in data["keywords"]:
            if keyword in lowered:
                return name
    return None


def _score_conditions(category: str, answers: dict):
    conditions = SYMPTOM_CATEGORIES[category]["conditions"]
    results = []
    for condition in conditions:
        indicators = condition["indicators"]
        total = len(indicators)
        matched = 0
        matched_details = []
        for question_id, expected_values in indicators.items():
            given = answers.get(question_id)
            if given in expected_values:
                matched += 1
                matched_details.append(given)
        score = matched / total if total else 0
        if score >= MATCH_THRESHOLD:
            results.append({
                "name": condition["name"],
                "score": score,
                "explanation": condition["explanation"],
                "first_aid": condition["first_aid"],
                "matched": matched_details,
            })
    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:3]


def handle_message(session_id: str, message: str) -> dict:
    """
    Main entry point. Returns a dict describing how the bot should respond:
    { type: 'emergency' | 'question' | 'result' | 'clarify', ... }
    """
    state = get_session(session_id)

    emergency_reason = check_emergency(message)
    if emergency_reason:
        clear_session(session_id)
        return {
            "type": "emergency",
            "reason": emergency_reason,
        }

    # Mid-questionnaire: treat message as the answer to the current question
    if state.category and state.question_index < len(state.questions):
        current_question = state.questions[state.question_index]
        answer = _match_option(message, current_question["options"])
        if answer is None:
            # Do not guess: ask the same question again
            return {"type": "question", "question": current_question, "retry": True}
        state.answers[current_question["id"]] = answer
        state.question_index += 1

        if state.question_index < len(state.questions):
            next_question = state.questions[state.question_index]
            return {"type": "question", "question": next_question}

        results = _score_conditions(state.category, state.answers)
        category_name = state.category
        clear_session(session_id)
        if not results:
            return {
                "type": "result",
                "conditions": [],
                "category": category_name,
            }
        return {
            "type": "result",
            "conditions": results,
            "category": category_name,
        }

    # Fresh concern: detect category
    category = _detect_category(message)
    if not category:
        return {"type": "clarify"}

    state.category = category
    state.questions = SYMPTOM_CATEGORIES[category]["questions"]
    state.question_index = 0
    state.answers = {}

    first_question = state.questions[0]
    return {"type": "question", "question": first_question}


def _match_option(message: str, options: list):
    """Match the user's reply to one of the options.
    Returns None if the reply cannot be matched, so the question is asked again
    instead of silently assuming an answer."""
    lowered = message.lower().strip()
    for option in options:
        if option in lowered or (len(lowered) >= 3 and lowered in option):
            return option
    # selection by number, e.g. "1", "2"
    if lowered.isdigit():
        index = int(lowered) - 1
        if 0 <= index < len(options):
            return options[index]
    # word overlap, e.g. "spreading to my arm" -> "pain spreading to arm or jaw"
    words = {w for w in lowered.replace("/", " ").split() if len(w) > 3}
    scores = [len(words & {w for w in o.replace("/", " ").split() if len(w) > 3}) for o in options]
    best = max(scores)
    if best > 0 and scores.count(best) == 1:
        return options[scores.index(best)]
    return None

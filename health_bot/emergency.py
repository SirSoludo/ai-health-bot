"""
Emergency keyword detection.
Runs on every user message before normal conversation logic.
"""

EMERGENCY_PATTERNS = {
    "difficulty breathing": "Severe breathing difficulty can be life-threatening.",
    "can't breathe": "Inability to breathe properly is a medical emergency.",
    "can't breath": "Inability to breathe properly is a medical emergency.",
    "cannot breath": "Inability to breathe properly is a medical emergency.",
    "not breathing": "A person who is not breathing needs emergency help immediately.",
    "trouble breathing": "Trouble breathing can be a sign of a serious condition and needs urgent assessment.",
    "struggling to breathe": "Struggling to breathe can be a sign of a serious condition and needs urgent assessment.",
    "hard to breathe": "Difficulty breathing can be a sign of a serious condition and needs urgent assessment.",
    "shortness of breath": "Shortness of breath can be a sign of a serious condition and needs urgent assessment.",
    "very short of breath": "Severe shortness of breath can be life-threatening and needs urgent assessment.",
    "cannot breathe": "Inability to breathe properly is a medical emergency.",
    "chest pain and": "Chest pain with additional symptoms may indicate a heart emergency.",
    "severe chest pain": "Severe chest pain may indicate a heart emergency.",
    "unconscious": "Loss of consciousness requires immediate emergency care.",
    "unresponsive": "An unresponsive person requires immediate emergency care.",
    "heavy bleeding": "Heavy or uncontrolled bleeding requires immediate emergency care.",
    "won't stop bleeding": "Uncontrolled bleeding requires immediate emergency care.",
    "severe allergic": "Severe allergic reactions can rapidly become life-threatening.",
    "swelling of face": "Facial or throat swelling can indicate a severe allergic reaction.",
    "throat closing": "Throat swelling can block the airway and is a medical emergency.",
    "seizure": "A seizure requires urgent medical attention.",
    "suicidal": "Thoughts of self-harm need immediate professional support.",
    "want to end my life": "Thoughts of self-harm need immediate professional support.",
    "overdose": "A suspected overdose requires immediate emergency care.",
    "stroke": "Signs of stroke require immediate emergency care.",
    "face drooping": "Facial drooping can be a sign of stroke.",
    "poisoned": "Suspected poisoning requires immediate emergency care.",
}


def check_emergency(text: str):
    """Returns a reason string if an emergency phrase is detected, else None."""
    lowered = text.lower()
    for phrase, reason in EMERGENCY_PATTERNS.items():
        if phrase in lowered:
            return reason
    return None

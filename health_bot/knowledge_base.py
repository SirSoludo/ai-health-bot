"""
Static rule-based knowledge base for the AI Health Bot.
Each symptom category has:
 - keywords: words used to detect the category from free text
 - questions: follow-up multiple choice questions
 - conditions: possible conditions with indicators used for scoring
"""

SYMPTOM_CATEGORIES = {

    "headache": {
        "keywords": ["headache", "migraine", "head pain", "head ache"],
        "questions": [
            {"id": "severity", "text": "How severe is the headache?",
             "options": ["mild", "moderate", "severe"]},
            {"id": "duration", "text": "How long have you had it?",
             "options": ["less than a day", "1-3 days", "more than 3 days"]},
            {"id": "extra", "text": "Do you also have any of these?",
             "options": ["nausea or vomiting", "sensitivity to light", "fever", "none"]},
        ],
        "conditions": [
            {
                "name": "Tension Headache",
                "indicators": {"severity": ["mild", "moderate"], "extra": ["none"]},
                "explanation": "Mild to moderate pain without nausea or light sensitivity commonly points to a tension headache, often caused by stress or muscle strain.",
                "first_aid": "Rest in a quiet room, stay hydrated, and consider a warm compress on the neck and shoulders.",
            },
            {
                "name": "Migraine",
                "indicators": {"severity": ["severe"], "extra": ["nausea or vomiting", "sensitivity to light"]},
                "explanation": "Severe headache pain combined with nausea or light sensitivity is a common pattern seen in migraines.",
                "first_aid": "Rest in a dark, quiet room and avoid screens. Cold compresses on the forehead may help.",
            },
            {
                "name": "Possible Viral Infection",
                "indicators": {"extra": ["fever"], "duration": ["1-3 days", "more than 3 days"]},
                "explanation": "A headache alongside fever lasting more than a day can suggest your body is fighting an infection.",
                "first_aid": "Rest, stay hydrated, and monitor your temperature.",
            },
        ],
    },

    "fever": {
        "keywords": ["fever", "temperature", "feverish", "hot body", "chills"],
        "questions": [
            {"id": "severity", "text": "How high does your temperature feel?",
             "options": ["mild warmth", "moderately hot", "very hot / shivering"]},
            {"id": "duration", "text": "How long has the fever lasted?",
             "options": ["less than a day", "1-3 days", "more than 3 days"]},
            {"id": "extra", "text": "Any other symptoms?",
             "options": ["cough or sore throat", "body aches", "rash", "none"]},
        ],
        "conditions": [
            {
                "name": "Common Viral Fever",
                "indicators": {"severity": ["mild warmth", "moderately hot"], "duration": ["less than a day", "1-3 days"]},
                "explanation": "A mild to moderate fever lasting a short time is typical of common viral illnesses.",
                "first_aid": "Rest, drink plenty of fluids, and monitor temperature regularly.",
            },
            {
                "name": "Possible Flu or Infection",
                "indicators": {"extra": ["body aches", "cough or sore throat"], "severity": ["moderately hot", "very hot / shivering"]},
                "explanation": "Fever combined with body aches or a sore throat/cough often indicates a flu-like infection.",
                "first_aid": "Rest, stay hydrated, and use a cool damp cloth to help manage discomfort.",
            },
            {
                "name": "Fever Requiring Prompt Attention",
                "indicators": {"severity": ["very hot / shivering"], "duration": ["more than 3 days"]},
                "explanation": "A very high fever that has lasted several days should be evaluated by a professional to rule out a serious infection.",
                "first_aid": "Keep cool, hydrate, and seek medical attention soon.",
            },
        ],
    },

    "stomach": {
        "keywords": ["stomach", "abdominal", "belly", "nausea", "vomiting", "diarrhea", "stomach ache", "stomach pain"],
        "questions": [
            {"id": "severity", "text": "How would you describe the pain?",
             "options": ["mild", "moderate", "severe"]},
            {"id": "duration", "text": "How long has this been going on?",
             "options": ["less than a day", "1-3 days", "more than 3 days"]},
            {"id": "extra", "text": "Any other symptoms?",
             "options": ["vomiting", "diarrhea", "blood in stool or vomit", "none"]},
        ],
        "conditions": [
            {
                "name": "Mild Indigestion",
                "indicators": {"severity": ["mild"], "extra": ["none"]},
                "explanation": "Mild pain without vomiting, diarrhea, or bleeding often points to indigestion or gas.",
                "first_aid": "Rest, avoid heavy or spicy meals, and sip water slowly.",
            },
            {
                "name": "Gastroenteritis (Stomach Bug)",
                "indicators": {"extra": ["vomiting", "diarrhea"], "duration": ["less than a day", "1-3 days"]},
                "explanation": "Vomiting and/or diarrhea over a short period commonly indicates gastroenteritis.",
                "first_aid": "Stay hydrated with small frequent sips of water or oral rehydration solution, and rest.",
            },
            {
                "name": "Condition Needing Urgent Review",
                "indicators": {"extra": ["blood in stool or vomit"], "severity": ["severe"]},
                "explanation": "Severe pain with visible blood is a warning sign that needs prompt medical evaluation.",
                "first_aid": "Avoid food, stay still, and seek medical attention as soon as possible.",
            },
        ],
    },

    "cough_cold": {
        "keywords": ["cough", "cold", "sore throat", "runny nose", "sneezing", "flu"],
        "questions": [
            {"id": "duration", "text": "How long have you had these symptoms?",
             "options": ["less than 3 days", "3-7 days", "more than a week"]},
            {"id": "severity", "text": "How would you describe your breathing?",
             "options": ["normal", "slightly short of breath", "very short of breath"]},
            {"id": "extra", "text": "Any other symptoms?",
             "options": ["fever", "chest tightness", "none"]},
        ],
        "conditions": [
            {
                "name": "Common Cold",
                "indicators": {"duration": ["less than 3 days", "3-7 days"], "severity": ["normal"]},
                "explanation": "Short-duration cough or cold symptoms with normal breathing usually indicate a common cold.",
                "first_aid": "Rest, warm fluids, and steam inhalation can ease symptoms.",
            },
            {
                "name": "Possible Flu",
                "indicators": {"extra": ["fever"], "duration": ["3-7 days", "more than a week"]},
                "explanation": "Cold-like symptoms combined with fever over several days may suggest the flu rather than a simple cold.",
                "first_aid": "Rest, hydrate, and monitor your temperature closely.",
            },
            {
                "name": "Respiratory Concern Needing Review",
                "indicators": {"severity": ["slightly short of breath", "very short of breath"], "extra": ["chest tightness"]},
                "explanation": "Breathing difficulty or chest tightness alongside cough symptoms should be assessed by a professional.",
                "first_aid": "Sit upright, stay calm, and seek medical attention if breathing worsens.",
            },
        ],
    },

    "skin": {
        "keywords": ["rash", "skin", "itch", "swelling", "allergy", "hives"],
        "questions": [
            {"id": "severity", "text": "How widespread is it?",
             "options": ["small localized area", "several areas", "covering most of the body"]},
            {"id": "extra", "text": "Any other symptoms?",
             "options": ["difficulty breathing", "swelling of face or lips", "itching only", "none"]},
            {"id": "duration", "text": "How long have you noticed it?",
             "options": ["less than a day", "1-3 days", "more than 3 days"]},
        ],
        "conditions": [
            {
                "name": "Mild Skin Irritation",
                "indicators": {"severity": ["small localized area"], "extra": ["itching only", "none"]},
                "explanation": "A small localized itchy area often suggests contact irritation or a mild allergic reaction.",
                "first_aid": "Avoid scratching, keep the area clean, and apply a cool compress.",
            },
            {
                "name": "Allergic Reaction",
                "indicators": {"severity": ["several areas", "covering most of the body"], "extra": ["itching only"]},
                "explanation": "A rash spreading across several areas of the body suggests a broader allergic reaction.",
                "first_aid": "Avoid the suspected trigger and monitor closely for worsening symptoms.",
            },
            {
                "name": "Severe Allergic Reaction (Possible Anaphylaxis)",
                "indicators": {"extra": ["difficulty breathing", "swelling of face or lips"]},
                "explanation": "Swelling of the face/lips or difficulty breathing alongside a rash can indicate a severe allergic reaction.",
                "first_aid": "This can be an emergency. Seek immediate medical attention.",
            },
        ],
    },

    "injury": {
        "keywords": ["injury", "cut", "wound", "burn", "sprain", "fall", "bruise", "bleeding"],
        "questions": [
            {"id": "type", "text": "What type of injury is it?",
             "options": ["cut or wound", "burn", "sprain or twist", "bruise"]},
            {"id": "severity", "text": "How would you describe it?",
             "options": ["minor", "moderate", "severe / heavy bleeding"]},
        ],
        "conditions": [
            {
                "name": "Minor Cut or Wound",
                "indicators": {"type": ["cut or wound"], "severity": ["minor", "moderate"]},
                "explanation": "A minor to moderate cut without heavy bleeding can typically be managed with basic first aid.",
                "first_aid": "Clean the wound with water, apply gentle pressure with a clean cloth, and cover with a sterile bandage.",
            },
            {
                "name": "Minor Burn",
                "indicators": {"type": ["burn"], "severity": ["minor", "moderate"]},
                "explanation": "A minor to moderate burn can often be cooled and cared for at home.",
                "first_aid": "Cool the burn under running water for 10-20 minutes. Do not apply ice, butter, or ointments. Cover loosely.",
            },
            {
                "name": "Sprain or Strain",
                "indicators": {"type": ["sprain or twist"]},
                "explanation": "Pain, swelling, or difficulty moving a joint after a twist typically indicates a sprain or strain.",
                "first_aid": "Follow R.I.C.E: Rest, Ice, Compression, Elevation. Avoid putting weight on the area.",
            },
            {
                "name": "Serious Injury Needing Immediate Care",
                "indicators": {"severity": ["severe / heavy bleeding"]},
                "explanation": "Heavy bleeding or a severe injury needs urgent professional attention.",
                "first_aid": "Apply firm, continuous pressure with a clean cloth and seek emergency care immediately.",
            },
        ],
    },

    "chest_pain": {
        "keywords": ["chest pain", "chest tightness", "chest discomfort"],
        "questions": [
            {"id": "severity", "text": "How severe is the chest pain?",
             "options": ["mild", "moderate", "severe"]},
            {"id": "extra", "text": "Do you also have any of these?",
             "options": ["shortness of breath", "pain spreading to arm or jaw", "sweating", "none"]},
        ],
        "conditions": [
            {
                "name": "Possible Muscle Strain",
                "indicators": {"severity": ["mild"], "extra": ["none"]},
                "explanation": "Mild chest discomfort without breathing difficulty or radiating pain may be muscular, but should still be watched.",
                "first_aid": "Rest and avoid strain. Seek medical advice if pain persists or worsens.",
            },
            {
                "name": "Potential Cardiac Emergency",
                "indicators": {"severity": ["moderate", "severe"], "extra": ["shortness of breath", "pain spreading to arm or jaw", "sweating"]},
                "explanation": "Chest pain with shortness of breath, radiating pain, or sweating are warning signs that require immediate emergency care.",
                "first_aid": "Sit the person down, keep them calm and still, and call emergency services immediately.",
            },
        ],
    },
}

MATCH_THRESHOLD = 0.4

def pre_screen_risk(form_data: dict) -> str:
    """
    Deterministic hard-trigger screening.
    Any single hard ethical trigger returns HIGH regardless of downstream LLM output.
    """
    text_blob = " ".join(str(v) for v in form_data.values()).lower()

    high_triggers = [
        "under 18", "minor", "children", "vulnerable adult", "vulnerable group",
        "deception", "covert", "without consent", "sensitive personal data",
        "special category data", "self-harm", "suicide", "trauma",
        "criminal history", "asylum seeker", "prisoner", "incapacity"
    ]

    medium_triggers = [
        "identifiable data", "audio recording", "video recording",
        "third-party data", "international transfer", "commercial funding"
    ]

    if any(trigger in text_blob for trigger in high_triggers):
        return "HIGH"
    elif any(trigger in text_blob for trigger in medium_triggers):
        return "MEDIUM"
    else:
        return "LOW"

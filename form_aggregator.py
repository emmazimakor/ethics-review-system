def aggregate_form_to_string(form_data: dict) -> str:
    sections = []
    for key, value in form_data.items():
        label = key.replace("_", " ").title()
        sections.append(f"{label}:\n{value}\n")
    return "\n".join(sections)


def check_for_todo(text):
    has_todo = "#TODO" in text.upper()
    return has_todo
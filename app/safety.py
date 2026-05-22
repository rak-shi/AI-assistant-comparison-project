blocked_words = [
    "bomb",
    "hack",
    "kill"
]

def safe_check(text):

    text = text.lower()

    for word in blocked_words:
        if word in text:
            return False

    return True
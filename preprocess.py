import re
#text preprocessing (lowercasing, regex-based cleaning).
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

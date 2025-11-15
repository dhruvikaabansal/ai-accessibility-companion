def detect_sentiment(text: str) -> dict:
    """
    Lightweight sentiment + difficulty detector for demo.
    """
    import re
    if not text or not text.strip():
        return {"sentiment": "neutral", "confidence": 1.0, "difficulty": "easy"}

    t = text.lower()

    positive = {"good", "happy", "awesome", "great", "love", "amazing", "fantastic", "nice", "well", "positive", "enjoy"}
    negative = {"bad", "sad", "terrible", "awful", "hate", "worst", "poor", "difficult", "problem", "angry"}

    # keep only word-characters for matching
    words = [re.sub(r'[^a-z0-9]', '', w) for w in t.split() if w.strip()]
    pos = sum(1 for w in words if w in positive)
    neg = sum(1 for w in words if w in negative)

    score = pos - neg
    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"

    wc = len(words)
    difficulty = "easy" if wc < 40 else "medium" if wc < 120 else "difficult"
    confidence = round(min(0.99, 0.5 + (abs(score) / max(1, wc))), 3)

    return {"sentiment": label, "confidence": confidence, "difficulty": difficulty, "word_count": wc}

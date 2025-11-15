def summarize_text(text: str, num_sentences: int = 2) -> str:
    import re
    if not text or not text.strip():
        return ""

    # naive sentence split
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    if len(parts) <= num_sentences:
        return text.strip()
    return " ".join(parts[:num_sentences]).strip()

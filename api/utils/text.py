def clean_string(text: str, pick_start: int, remove_spaces: bool = True) -> str:
    """Strip leading words and optionally remove all whitespace from a string."""
    words = text.split()
    if len(words) > pick_start:
        words = words[pick_start:]
    joined = "".join(words)
    return joined.replace(" ", "") if remove_spaces else joined

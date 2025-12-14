import re


def surface_analysis(text: str) -> dict:
    # ---- basic counts ----
    char_count = len(text)
    word_count = len(text.split())
    line_count = text.count("\n") + 1 if text else 0

    # ---- sentence approximation ----
    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]
    sentence_count = len(sentences)

    avg_words_per_sentence = (
        word_count / sentence_count if sentence_count > 0 else 0
    )

    # ---- fragmentation indicators ----
    ellipsis_count = text.count("...")
    newline_density = (
        text.count("\n") / char_count if char_count > 0 else 0
    )

    return {
        "length": {
            "characters": char_count,
            "words": word_count,
            "lines": line_count,
        },
        "fragmentation": {
            "sentences": sentence_count,
            "avg_words_per_sentence": round(avg_words_per_sentence, 2),
            "ellipsis_count": ellipsis_count,
            "newline_density": round(newline_density, 4),
        },
    }

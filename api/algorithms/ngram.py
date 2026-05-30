from nltk.util import ngrams


def ngram_similarity(query: str, document: str, n: int = 3) -> float:
    """Jaccard similarity over character n-grams of two strings."""
    query_ngrams = set(ngrams(query.lower(), n))
    document_ngrams = set(ngrams(document.lower(), n))

    if not query_ngrams or not document_ngrams:
        return 0.0

    intersection = query_ngrams & document_ngrams
    union = query_ngrams | document_ngrams
    return len(intersection) / len(union)

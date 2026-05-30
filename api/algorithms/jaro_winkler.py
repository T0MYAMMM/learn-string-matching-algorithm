from typing import List, Tuple

import pandas as pd
from pyjarowinkler import distance


def jaro_winkler_search(
    series: pd.Series,
    pattern: str,
    threshold: float = 0.8,
) -> List[Tuple[int, float]]:
    """Return (index, similarity) pairs whose Jaro-Winkler score meets threshold."""
    results: List[Tuple[int, float]] = []

    for idx, value in series.items():
        try:
            similarity = distance.get_jaro_distance(value, pattern, winkler=True, scaling=0.1)
        except Exception:
            continue

        if similarity is not None and similarity >= threshold:
            results.append((idx, similarity))

    results.sort(key=lambda x: x[1], reverse=True)
    return results

from typing import List, Tuple

import pandas as pd
from fuzzywuzzy import process as fuzzywuzzy_process


def fuzzy_search(
    query: str,
    names: pd.Series,
    limit: int = 10,
) -> List[Tuple[str, int, int]]:
    """Return top matches using fuzzywuzzy token-set ratio."""
    return fuzzywuzzy_process.extract(query, names, limit=limit)

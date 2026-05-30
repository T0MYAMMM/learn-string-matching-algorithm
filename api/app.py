import os
import time
from typing import Any, Dict

import pandas as pd
from flask import Flask, jsonify, render_template, request

from algorithms import fuzzy_search, jaro_winkler_search, ngram_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

app = Flask(__name__, template_folder="templates", static_folder="static")

hospitals: pd.DataFrame = pd.read_json(os.path.join(DATA_DIR, "rumahsakit_medicalclinicid_cleaned.json"))


def _search(series: pd.Series, query: str, threshold: float = 0.5) -> Dict[str, Any]:
    """Run all three algorithms and return results with timing."""
    results: Dict[str, list] = {}
    timings: Dict[str, float] = {}

    start = time.perf_counter()
    raw_fuzzy = fuzzy_search(query, series)
    timings["fuzzy"] = time.perf_counter() - start
    results["fuzzy"] = [[match[2], match[1]] for match in raw_fuzzy]

    start = time.perf_counter()
    results["ngram"] = [
        [idx, round(ngram_similarity(query, value), 2)]
        for idx, value in series.items()
        if ngram_similarity(query, value) >= threshold
    ]
    timings["ngram"] = time.perf_counter() - start

    start = time.perf_counter()
    results["jarowinkler"] = jaro_winkler_search(series, query)
    timings["jarowinkler"] = time.perf_counter() - start

    return results, timings


@app.route("/")
def home():
    return render_template("index.html", results=hospitals.to_dict(orient="records"))


@app.route("/search_rumahsakit", methods=["POST"])
def search_hospitals():
    query = request.form.get("query", "").strip()

    if not query:
        return jsonify({"results": {}, "score": {}, "processing_times": {}})

    raw_results, timings = _search(hospitals["Nama Rumah Sakit"], query)

    results_df = {
        algorithm: hospitals.loc[[idx for idx, _ in indices]].to_dict(orient="records")
        for algorithm, indices in raw_results.items()
    }
    scores = {
        algorithm: [[idx, score] for idx, score in indices]
        for algorithm, indices in raw_results.items()
    }

    return jsonify({"results": results_df, "score": scores, "processing_times": timings})


if __name__ == "__main__":
    app.run(debug=True)

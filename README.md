# String Matching Algorithm Comparison

A Flask web application that benchmarks three string-matching algorithms against a dataset of Indonesian hospitals. Given a search query, the app runs Fuzzy, N-gram, and Jaro-Winkler searches in parallel, returns ranked results for each algorithm, and reports per-algorithm processing times so users can directly compare their accuracy and performance.

## Architecture / Tech Stack

| Layer | Technology |
|---|---|
| Web framework | Flask 2.2 |
| Data processing | pandas 2.0 |
| Fuzzy matching | fuzzywuzzy + python-Levenshtein |
| N-gram matching | NLTK |
| Jaro-Winkler | pyjarowinkler |
| Frontend | Bootstrap 4, jQuery |
| Deployment | Vercel (serverless Python) |

## Project Structure

```
learn-string-matching-algorithm/
├── api/
│   ├── app.py                  # Flask application and route handlers
│   ├── algorithms/
│   │   ├── __init__.py
│   │   ├── fuzzy.py            # fuzzywuzzy-based search
│   │   ├── ngram.py            # character n-gram Jaccard similarity
│   │   └── jaro_winkler.py     # Jaro-Winkler distance search
│   ├── utils/
│   │   ├── __init__.py
│   │   └── text.py             # string cleaning helpers
│   ├── data/
│   │   ├── rumahsakit_medicalclinicid_cleaned.json
│   │   ├── rumahsakit_medicalclinicid_cleaned.csv
│   │   ├── apotek_medicalclinicid_cleaned.csv
│   │   └── penyakit_medicalclinicid_cleaned.csv
│   ├── static/css/main.css
│   └── templates/index.html
├── scripts/
│   └── convert_data.py         # CSV-to-JSON conversion utility
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── vercel.json
```

## Local Setup and Installation

**Prerequisites:** Python 3.9+

1. Clone the repository:
   ```bash
   git clone https://github.com/T0MYAMMM/learn-string-matching-algorithm.git
   cd learn-string-matching-algorithm
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy the environment file:
   ```bash
   cp .env.example .env
   ```

5. Run the development server from the `api/` directory:
   ```bash
   cd api
   python app.py
   ```

   The app will be available at `http://127.0.0.1:5000`.

## Usage

Open the app in a browser and type a hospital name (partial or misspelled) into the search bar. Clicking **Search** sends the query to the `/search_rumahsakit` endpoint, which returns results from all three algorithms side-by-side along with their match scores and processing times.

To regenerate the JSON data file from the CSV source:

```bash
python scripts/convert_data.py \
    api/data/rumahsakit_medicalclinicid_cleaned.csv \
    api/data/rumahsakit_medicalclinicid_cleaned.json
```

## Future Improvements

- Add a scoring benchmark page that measures precision and recall for each algorithm against a labelled query set.
- Extend the dataset to include the pharmacy (`apotek`) and disease (`penyakit`) CSVs with dedicated search routes.
- Replace fuzzywuzzy with RapidFuzz for a significant performance improvement without API changes.
- Introduce pagination on search results to handle large result sets more gracefully.
- Add a CI pipeline with linting (ruff) and unit tests covering each algorithm module.
- Support configurable algorithm weights so users can tune a combined ranking score.

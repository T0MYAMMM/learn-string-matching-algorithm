"""One-off script: convert a hospital CSV to JSON for the API."""

import argparse
import os

import pandas as pd


def convert_csv_to_json(csv_path: str, json_path: str) -> None:
    data = pd.read_csv(csv_path)
    data.to_json(json_path, orient="records", force_ascii=False, indent=2)
    print(f"Converted {csv_path} -> {json_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert hospital CSV to JSON.")
    parser.add_argument("csv", help="Path to input CSV file")
    parser.add_argument("json", help="Path to output JSON file")
    args = parser.parse_args()

    if not os.path.isfile(args.csv):
        raise FileNotFoundError(f"CSV file not found: {args.csv}")

    convert_csv_to_json(args.csv, args.json)

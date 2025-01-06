# Copyright 2025 by Miriam Balzer & Julian Welling, University of Duisburg-Essen
# Licensed under the MIT License
# This file may be copied, modified, and distributed under the terms of the MIT License.


from json import loads, dump
import argparse
import os

from workflow.table_handler import load_raw_table, set_MIC_index, shrink_clean_table


def save_as_json(input_table, path):
    # Ensure the output directory exists
    output_dir = os.path.dirname(path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it doesn't exist

    vanilla_json = input_table.to_json(orient="records")
    parsed_json = loads(vanilla_json)
    with open(path, "w", encoding="utf-8") as json_file: dump(parsed_json, json_file, ensure_ascii=False, indent=4)

def process(input_path, sheet_name):
    raw_table = load_raw_table(input_path, sheet_name)
    mic_table = set_MIC_index(raw_table)
    shrunk_table = shrink_clean_table(mic_table)
    return shrunk_table

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process MIC tables from an Excel workbook.")
    parser.add_argument("input_path", type=str, help="Path to the Excel file.")
    parser.add_argument("sheet_name", type=str, help="Name of the sheet to process.")
    parser.add_argument("output_path", type=str, help="Path to save the output JSON.")
    args = parser.parse_args()

    shrunk_table = process(args.input_path, args.sheet_name)
    save_as_json(shrunk_table, args.output_path)
    print(f"JSON saved to {args.output_path}")

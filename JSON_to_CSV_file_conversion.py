# JSON to CSV Conversion

import json
import csv
import os

def json_to_csv(json_file):
    # Extract file name without extension
    csv_file = os.path.splitext(json_file)[0] + ".csv"

    # Open the JSON file and load data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract all possible headers from the data in the order of appearance
    headers = []
    for item in data:
        for key in item.keys():
            if key not in headers:
                headers.append(key)

    # Open CSV file for writing
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)

        # Write header
        writer.writeheader()

        # Write data rows
        for row in data:
            # Fill missing values with empty strings
            row_data = {header: row.get(header, '') for header in headers}
            writer.writerow(row_data)

    print(f"Here's the newly generated CSV file path: '{csv_file}'")

# Provide JSON files path that you want to covert
json_file = r'C:\Users\xxxxxxx\Downloads\JSON_to_CSV_file_conversion\sample.json'
json_to_csv(json_file)
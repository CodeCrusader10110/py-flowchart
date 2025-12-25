"""
Module to create the import text for draw.io
"""
import secrets
import string
import json
import csv

def build_flowchart():
    # TODO docstring
    pass

# Path to your input JSON file
input_json_file = 'your_data.json'  # Replace with the actual filename

# Path to the output CSV file
output_csv_file = 'output.csv'

# Load the JSON data
with open(input_json_file, 'r') as f:
    data = json.load(f)

# Open the CSV file for writing
with open(output_csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Write the header row
    writer.writerow(['id', 'label', 'refs', 'style'])
    
    # Iterate over each node in the JSON object
    for node_id, info in data.items():
        # Convert refs list to a comma-separated string (empty if list is empty)
        refs_str = ','.join(info['refs']) if info['refs'] else ''
        
        # Write the row
        writer.writerow([node_id, info['label'], refs_str, info['style']])

print(f"CSV file '{output_csv_file}' created successfully!")
import csv
import json

with open('input.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('output.json', 'w') as f:
    json.dump(rows, f)

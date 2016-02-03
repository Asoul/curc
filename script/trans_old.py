import csv
import json
import time
from datetime import datetime
import unicodecsv

json_file = open("../Record.json", "r")
data = json.load(json_file)

field_names = [
    "createdAt",
    "bank",
    "AUD",
    "AUDout",
    "CAD",
    "CADout",
    "CHF",
    "CHFout",
    "CNY",
    "CNYout",
    "EUR",
    "EURout",
    "GBP",
    "GBPout",
    "HKD",
    "HKDout",
    "JPY",
    "JPYout",
    "NZD",
    "NZDout",
    "SEK",
    "SEKout",
    "SGD",
    "SGDout",
    "THD",
    "THDout",
    "USD",
    "USDout",
    "ZAR",
    "ZARout"
]

# Load file
csv_file = open('../data/record.csv', 'w')
writer = unicodecsv.DictWriter(csv_file,
    fieldnames=field_names, extrasaction='ignore')

rows = []
for row in data["results"]:
    rows.append(row)

# Sort by time
rows.sort(key=lambda row:
    time.mktime(datetime.strptime(row["createdAt"],
        "%Y-%m-%dT%H:%M:%S.%fZ").timetuple()))

# Write file
writer.writeheader()
for row in rows:
    writer.writerow(row)

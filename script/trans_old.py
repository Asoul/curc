import csv
import json
import unicodecsv

json_file = open("../Record.json", "r")
data = json.load(json_file)

field_names = [
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
    "ZARout",
    "bank",
    "createdAt",
    "isSuccess",
    "message",
    "objectId",
    "updateTime",
    "updatedAt",
]

csv_file = open('../data/record.csv', 'w')
writer = unicodecsv.DictWriter(csv_file, fieldnames=field_names)

writer.writeheader()

for row in data["results"]:
    writer.writerow(row)

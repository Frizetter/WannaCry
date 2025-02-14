import json

day = "15.02.2024"
name = "write a book"
timestart = "1100"
timefinish = "1200"

try:
    with open('secondarytable.json', 'r') as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {}

if day not in data:
    data[day] = {}
data[day][name] = {'timestart':timestart, 'timefinish':timefinish}

with open('secondarytable.json', 'w') as f:
    json.dump(data, f, indent=4)

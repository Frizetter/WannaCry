import json

with open('maintable.json', encoding='utf-8') as f:
    data = json.load(f)
for item in data['friday']:
    line = f'{item} {data['friday'][item]['timestart']} {data['friday'][item]['timefinish']}' 
    print(line)
import json

data = {
    'name': 'Oleh',
    'surname': 'Yemelianov',
    'age': 20,
    'year_of_birth': 2003,
    'speciality': 'Python Developer'
}

data_json = json.dumps(data)
print(f'Converted data into JSON: {data_json}')

with open('info.json', 'w', encoding='utf-8') as f:
    json.dump(data_json, f, ensure_ascii=False)

with open('info.json', 'r', encoding='utf-8') as file:
    new_file = json.load(file)
    print(f'Load data from JSON file: {new_file}')
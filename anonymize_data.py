import json
import random
import string

# Helper to generate anonymized names
def random_name(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Load people_data.json
with open('people_data.json', encoding='utf-8') as f:
    people_data = json.load(f)

people = people_data['people']
exclusions = people_data['exclusions']

# Create anonymized names as A, B, C, ...
anon_names = [chr(ord('A') + i) for i in range(len(people))]
name_map = dict(zip(people, anon_names))

# Anonymize people_data.json
anon_people_data = {
    'people': anon_names,
    'exclusions': [[name_map.get(ex, ex) for ex in excl] for excl in exclusions]
}

with open('people_data.anon.json', 'w', encoding='utf-8') as f:
    json.dump(anon_people_data, f, ensure_ascii=False, indent=2)

# Load allocation_results.json
with open('allocation_results.json', encoding='utf-8') as f:
    allocations = json.load(f)

# Anonymize allocation_results.json
anon_allocations = {name_map[k]: [name_map.get(x, x) for x in v] for k, v in allocations.items()}

with open('allocation_results.anon.json', 'w', encoding='utf-8') as f:
    json.dump(anon_allocations, f, ensure_ascii=False, indent=2)

print('Anonymized files written: people_data.anon.json, allocation_results.anon.json')

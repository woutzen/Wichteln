"""
Outzenwichteln: Allocate each person to give to and receive from exactly 2 others, respecting exclusions.
"""
import random
import json

with open('people_data.json', encoding='utf-8') as f:
    data = json.load(f)
    people_names = data['people']
    exclusions_names = data['exclusions']

# Use names directly instead of Enum
people_list = people_names
exclusions = exclusions_names

def print_exclusion_matrix(people, exclusions):
    print("Exclusion matrix (1 = can give, 0 = cannot):")
    for i, excl in enumerate(exclusions):
        row = [0 if (person in excl or i == j) else 1 for j, person in enumerate(people)]
        print(row)

print_exclusion_matrix(people_list, exclusions)

def find_valid_allocation(people, exclusions, max_tries=10000):
    n = len(people)
    possible = [
        [p for p in people if p != person and p not in exclusions[i]]
        for i, person in enumerate(people)
    ]
    for _ in range(max_tries):
        allocation = {person: [] for person in people}
        allocated_to = {person: set() for person in people}
        order = people[:]
        random.shuffle(order)
        success = True
        for person in order:
            choices = [
                p for p in possible[people.index(person)]
                if len(allocated_to[p]) < 2 and p not in allocation[person]
            ]
            if len(choices) < 2:
                success = False
                break
            selected = random.sample(choices, 2)
            allocation[person] = selected
            for sel in selected:
                allocated_to[sel].add(person)
        if success and all(len(allocated_to[p]) == 2 for p in people):
            return allocation
    return None

allocations = find_valid_allocation(people_list, exclusions)

# Save allocations to a JSON file
if allocations is not None:
    with open('allocation_results.json', 'w', encoding='utf-8') as f:
        json.dump(allocations, f, ensure_ascii=False, indent=2)

print("\nRandom allocation (each person gives to and receives from exactly 2, respecting exclusions):")
if allocations is None:
    print("No valid allocation found after many tries.")
else:
    for person, assigned in allocations.items():
        print(f"{person}: {assigned}")

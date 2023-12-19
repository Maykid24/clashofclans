import json


def attack_count(file_name):
    file_path = file_name

    with open(file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    data = json_data

    attacks_count_per_member = {}

    for member in data['clan']['members']:
        member_name = member['name']
        attacks_count = len(member.get('attacks', []))
        attacks_count_per_member[member_name] = attacks_count

    sorted_results = sorted(attacks_count_per_member.items(), key=lambda x: x[1])

    for member_name, attacks_count in sorted_results:
        print(f"{member_name}: {attacks_count} attacks")
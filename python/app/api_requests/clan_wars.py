import requests
import json
import os
import yaml
from datetime import datetime


def configuration_file():
    with open('python/app/config/config.yaml', 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        clan_api = data.get('clan_api')
        clan_tag = data.get('clan_id')
        return clan_api, clan_tag

def bearer():
    if os.path.isfile('token.json'):
        with open('token.json', 'r') as json_file:
            token = json.load(json_file)
            bearer_token = token.get('bearer_token')
            return bearer_token
    elif os.path.isfile('token.php'):
        with open('token.php') as php_file:
            php_content = php_file.read()
            start_index = php_content.find("'bearer_token' => '") + len("'bearer_token' =>'")
            end_index = php_content.find("'", start_index)
            bearer_token = php_content[start_index:end_index]
            return bearer_token
    else:
        print("NOOOOPE")
        return None


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

    result_json = {"attack_count_per_member": [{"member_name": name, "attacks_count": count} for name, count in sorted_results]}

    current_date = datetime.now().strftime('%Y-%m-%d')
    output_filename = f'clan_war_{current_date}.json'

    with open(output_filename, 'w') as output_file:
        json.dump(result_json, output_file, indent=2)


def call_api():
    token = bearer()
    clan_api, clan_tag = configuration_file()

    clan_url = f'{clan_api}%23' + clan_tag[1:] + '/currentwar'
    
    headers = {
        'Authorization': f'Bearer {token}'
    } 

    response = request

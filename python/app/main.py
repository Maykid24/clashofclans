import requests
import json
from datetime import datetime


with open('python/app/token_json.json', 'r') as json_file:
    config_data = json.load(json_file)

bearer_token = config_data.get('bearer_token')

folder_directory = 'python/json_files/'
current_date = datetime.now().strftime('%Y-%m-%d')

file_name = f'clan_war_{current_date}.json'
file_path = folder_directory + file_name


base_url = 'https://api.clashofclans.com/v1/'

player_tag = '#G9VURJR9G'
player_url = f'{base_url}players/%23' + player_tag[1:]

headers = {
    'Authorization': f'Bearer {bearer_token}'
}

response = requests.get(player_url, headers=headers)

with open(file_path, 'w') as json_write:
    json.dump(response.json(), json_write, indent=2)



if response.status_code == 200:
    player_data = response.json()
    print(player_data)
else:
    print(f'Error: {response.status_code}')
    print(response.text)

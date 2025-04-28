# How to connect to an API using python
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrieve data {response.status_code}")
    print(response.json)

pokemon_name = "pikachu"
pokemon_name2 = "typhlosion"

pokemon_info = get_pokemon_info(pokemon_name)
pokemon_info2 = get_pokemon_info(pokemon_name2)

if pokemon_info:
    print(f"{pokemon_info['name']}")
    print(f"{pokemon_info['id']}")
    print(f"{pokemon_info['height']}")
    print(f"{pokemon_info['weight']}")
    
    
if pokemon_info2:
    print(f"{pokemon_info2['name']}")
    print(f"{pokemon_info2['id']}")
    print(f"{pokemon_info2['height']}")
    print(f"{pokemon_info2['weight']}")  
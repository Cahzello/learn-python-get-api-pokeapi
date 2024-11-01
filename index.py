import requests
import json

def get_pokemon_data(pokemon_name):
    if not pokemon_name:
        raise ValueError("pokemon_name cannot be empty")
    print(f"Getting data for {pokemon_name}...")
    print("Fetching data from PokeAPI...")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(f"{pokemon_name.lower()}.json", "w") as json_file:
            json.dump(data, json_file)
        print(f"Data saved to {pokemon_name.lower()}.json")
        return True
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return False

# Example usage:
get_pokemon_data(input("Masukan nama pokemon: "))

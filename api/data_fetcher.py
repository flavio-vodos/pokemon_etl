import requests

def get_pokemon_data(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon = {
            'ID': data['id'],
            'Name': data['name'],
            'Height': data['height'],
            'Weight': data['weight'],
            'Base Experience': data['base_experience'],
            'Types': ', '.join([t['type']['name'] for t in data['types']])
        }
        return pokemon
    else:
        print(f'Erro ao obter dados do Pokémon com ID {pokemon_id}')
        return None
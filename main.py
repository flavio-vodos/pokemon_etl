import api.data_fetcher as data_fetcher
import data.data_handler as data_handler
import database.db_handler as db_handler

if __name__ == '__main__':
    pokemon_id = int(input('Digite o ID do Pokémon que deseja buscar: '))
    pokemon_data = data_fetcher.get_pokemon_data(pokemon_id)
    if pokemon_data:
        data_handler.save_to_csv(pokemon_data)
        db_handler.save_to_sqlite(pokemon_data)
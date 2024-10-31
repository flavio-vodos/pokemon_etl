import pandas as pd
import os

def save_to_csv(pokemon_data, filename='data/pokemon_data.csv'):
    # Garantir que o diretório existe
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # Salvar os dados no CSV
    if not os.path.exists(filename):
        df = pd.DataFrame([pokemon_data])
        df.to_csv(filename, index=False)
    else:
        df = pd.DataFrame([pokemon_data])
        df.to_csv(filename, index=False, mode='a', header=False)
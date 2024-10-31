import sqlite3
import os
import pandas as pd

def save_to_sqlite(pokemon_data, db_name='data/pokemon_data.db'):
    # Garantir que o diretório existe
    os.makedirs(os.path.dirname(db_name), exist_ok=True)
    # Salvar os dados no SQLite
    conn = sqlite3.connect(db_name)
    df = pd.DataFrame([pokemon_data])
    df.to_sql('pokemon', conn, if_exists='append', index=False)
    conn.close()
import pandas as pd
import os

json_path = 'api/TelecomX_Data.json'

if os.path.getsize(json_path) == 0:
    print("JSON file is empty.")
    dados = None
else:
    try:
        dados = pd.read_json(json_path)
        print(dados)
    except ValueError as e:
        print(f"Error reading JSON: {e}")
        dados = None
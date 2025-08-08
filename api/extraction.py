import pandas as pd
import json
from json_flattener import flatten

# Carregar o arquivo JSON
with open("api/TelecomX_Data.json", "r") as f:
    data = json.load(f)

# Converter o conteúdo em DataFrame
if isinstance(data, list):
    df = pd.DataFrame(data)
elif isinstance(data, dict):
    for key in data:
        if isinstance(data[key], list):
            df = pd.DataFrame(data[key])
            break
    else:
        df = pd.DataFrame([data])
else:
    raise ValueError("Formato de JSON não suportado.")

import json

def mostrar_aninhamentos(d, caminho=""):
    if isinstance(d, dict):
        for chave, valor in d.items():
            novo_caminho = f"{caminho}.{chave}" if caminho else chave
            if isinstance(valor, dict):
                print(f"Objeto aninhado em: {novo_caminho} (dict)")
                mostrar_aninhamentos(valor, novo_caminho)
            elif isinstance(valor, list):
                print(f"Lista aninhada em: {novo_caminho} (list)")
                mostrar_aninhamentos(valor, novo_caminho)
    elif isinstance(d, list):
        for i, item in enumerate(d):
            novo_caminho = f"{caminho}[{i}]"
            if isinstance(item, dict):
                print(f"Objeto aninhado em: {novo_caminho} (dict)")
                mostrar_aninhamentos(item, novo_caminho)
            elif isinstance(item, list):
                print(f"Lista aninhada em: {novo_caminho} (list)")
                mostrar_aninhamentos(item, novo_caminho)


mostrar_aninhamentos(data)


# Informações iniciais
print("Dimensões:", df.shape)
print("\nColunas:", df.columns)
print("\nValores ausentes:\n", df.isnull().sum())
print("\nTipos de dados:\n", df.dtypes)
print("\nPrimeiras linhas:\n", df.head())

flat = flatten(data)
for k in flat:
    print(k)


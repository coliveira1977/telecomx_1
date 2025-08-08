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



# Informações iniciais
print("Dimensões:", df.shape)
print("\nColunas:", df.columns)
print("\nValores ausentes:\n", df.isnull().sum())
print("\nTipos de dados:\n", df.dtypes)
print("\nPrimeiras linhas:\n", df.head())

#flat = flatten(data)
#for k in flat:
#    print(k)

def encontrar_colunas(data, caminho="api/TelecomX_Data.json"):
    colunas = set()
    
    if isinstance(data, dict):
        for chave, valor in data.items():
            novo_caminho = f"{caminho}.{chave}" if caminho else chave
            colunas.update(encontrar_colunas(valor, novo_caminho))
    
    elif isinstance(data, list):
        for item in data:
            colunas.update(encontrar_colunas(item, caminho))
    
    else:
        colunas.add(caminho)
    
    return colunas

# Carrega o JSON do arquivo
with open('api/TelecomX_Data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Executa a função e mostra o resultado
colunas_encontradas = encontrar_colunas(data)
print("Colunas aninhadas encontradas:")
for coluna in sorted(colunas_encontradas):
    print("-", coluna)
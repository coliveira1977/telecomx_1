import pandas as pd

# 1. Carrega o arquivo JSON (substitua pelo caminho do seu arquivo)
caminho_json = 'api/TelecomX_Data.json'
df = pd.read_json(caminho_json)

# 2. Identifica colunas que contêm dicts
colunas_aninhadas = [col for col in df.columns if df[col].apply(lambda x: isinstance(x, dict)).any()]

# 3. Normaliza cada coluna aninhada e adiciona prefixos
colunas_normalizadas = [
    pd.json_normalize(df[col].fillna({}), sep='_').add_prefix(f"{col}_")
    for col in colunas_aninhadas
]

# 4. DataFrame Normalizado (Colunas Desaninhadas)
df_normalizado = pd.concat([df.drop(columns=colunas_aninhadas)] + colunas_normalizadas, axis=1)

# 5. Visualiza o resultado

print("Dimensões:", df_normalizado.shape)
print("\nColunas:", df_normalizado.columns)
print("\nValores ausentes:\n", df_normalizado.isnull().sum())
print("\nTipos de dados:\n", df_normalizado.dtypes)
print("\nPrimeiras linhas:\n", df_normalizado.head())
df_normalizado.to_csv('telecomx_normalizado.csv', index=False)

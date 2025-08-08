import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Caminho do arquivo CSV
caminho_csv = 'telecomx_normalizado.csv'  # Substitua pelo seu caminho real

# 2. Carregar os dados
df = pd.read_csv(caminho_csv)

# 3. Verificar se a coluna 'Churn' existe
if 'Churn' not in df.columns:
    raise ValueError("❌ A coluna 'Churn' não foi encontrada no arquivo CSV.")

# 4. Mostrar primeiras linhas
print("\n🔍 Primeiras linhas do dataset:")
print(df.head())

# 5. Informações gerais
print("\n📋 Informações do DataFrame:")
print(df.info())

# 6. Valores ausentes
print("\n❓ Valores ausentes por coluna:")
print(df.isnull().sum())

# 7. Tipos de colunas
colunas_numericas = df.select_dtypes(include='number').columns.tolist()
colunas_categoricas = df.select_dtypes(exclude='number').columns.tolist()

# Remove 'Churn' da lista de categóricas se estiver lá
if 'Churn' in colunas_categoricas:
    colunas_categoricas.remove('Churn')

print("\n🔢 Colunas numéricas:", colunas_numericas)
print("🔤 Colunas categóricas:", colunas_categoricas)

# 8. Distribuição de Churn
print("\n📊 Distribuição da variável 'Churn':")
print(df['Churn'].value_counts(normalize=True))

# Gráfico de barras da distribuição de Churn
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Churn')
plt.title('Distribuição da variável Churn')
plt.xlabel('Churn')
plt.ylabel('Contagem')
plt.show()

# 9. Estatísticas por grupo de Churn
print("\n📈 Estatísticas das variáveis numéricas por 'Churn':")
print(df.groupby('Churn')[colunas_numericas].mean())

# 10. Correlação com 'Churn' (se for numérica ou binária)
if df['Churn'].dtype in ['int64', 'float64'] or df['Churn'].nunique() == 2:
    # Converter Churn para numérico se for necessário
    if df['Churn'].dtype == 'object':
        df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1}).fillna(0)

    correlacoes = df.corr(numeric_only=True)['Churn'].sort_values(ascending=False)
    print("\n🔗 Correlação com 'Churn':")
    print(correlacoes)

    # Gráfico de barras das correlações
    plt.figure(figsize=(8, 6))
    correlacoes.drop('Churn').plot(kind='barh')
    plt.title('Correlação das variáveis com Churn')
    plt.xlabel('Correlação')
    plt.grid(True)
    plt.show()

# 11. Boxplots das variáveis numéricas por Churn
for coluna in colunas_numericas:
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x='Churn', y=coluna)
    plt.title(f'{coluna} por Churn')
    plt.xlabel('Churn')
    plt.ylabel(coluna)
    plt.show()

# 12. Gráficos de contagem para variáveis categóricas
for coluna in colunas_categoricas:
    plt.figure(figsize=(7, 4))
    sns.countplot(data=df, x=coluna, hue='Churn')
    plt.title(f'{coluna} vs Churn')
    plt.xlabel(coluna)
    plt.ylabel('Contagem')
    plt.legend(title='Churn')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

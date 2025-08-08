import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import os

# Caminho para o CSV no seu Mac
caminho_csv = '/Users/chris/telecomx_1/telecomx_normalizado.csv'
df = pd.read_csv(caminho_csv)

# Verificar a existência da coluna Churn
if 'Churn' not in df.columns:
    raise ValueError("A coluna 'Churn' não foi encontrada.")

# Preparar PDF
pdf_path = '/Users/chris/telecomx_1/relatorio_churn_completo.pdf'
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Título
story.append(Paragraph("📊 Relatório de Análise de Churn", styles['Title']))
story.append(Spacer(1, 12))

# Gráfico de contagem de Churn
story.append(Paragraph("1. Distribuição da variável 'Churn'", styles['Heading2']))
story.append(Paragraph("Este gráfico mostra a quantidade de clientes que permaneceram e que saíram.", styles['BodyText']))
plt.figure(figsize=(4, 3))
sns.countplot(data=df, x='Churn')
plt.title("Distribuição de Churn")
plt.tight_layout()
plt.savefig("grafico_churn.png")
plt.close()
story.append(Image("grafico_churn.png", width=400, height=300))
story.append(Spacer(1, 12))

# Correlação
if df['Churn'].dtype == 'object':
    df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1}).fillna(0)

correlacoes = df.corr(numeric_only=True)['Churn'].sort_values(ascending=False).drop('Churn')
story.append(Paragraph("2. Correlação com a variável 'Churn'", styles['Heading2']))
story.append(Paragraph("Mostra quais variáveis numéricas mais se correlacionam com a saída de clientes.", styles['BodyText']))
correlacoes.plot(kind='barh', title='Correlação com Churn')
plt.xlabel("Correlação")
plt.tight_layout()
plt.savefig("grafico_correlacao.png")
plt.close()
story.append(Image("grafico_correlacao.png", width=400, height=300))
story.append(Spacer(1, 12))

# Guardar explicações dos principais fatores de churn
explicacoes = []
top_variaveis = correlacoes.head(5)

for var, corr in top_variaveis.items():
    direcao = "aumenta" if corr > 0 else "reduz"
    explicacoes.append(f"A variável '{var}' tem uma correlação de {corr:.2f} com o Churn, o que sugere que seu aumento tende a {direcao} a chance de um cliente sair.")

# Boxplots das variáveis numéricas
story.append(Paragraph("3. Distribuições por 'Churn'", styles['Heading2']))
story.append(Paragraph("Boxplots mostram como as distribuições de variáveis numéricas diferem entre clientes que saem e os que ficam.", styles['BodyText']))
colunas_numericas = df.select_dtypes(include='number').columns.tolist()
for coluna in colunas_numericas:
    if coluna == 'Churn':
        continue
    plt.figure(figsize=(4, 3))
    sns.boxplot(data=df, x='Churn', y=coluna)
    plt.title(f"{coluna} por Churn")
    plt.tight_layout()
    nome_arquivo = f"boxplot_{coluna}.png"
    plt.savefig(nome_arquivo)
    plt.close()
    story.append(Paragraph(f"Boxplot: {coluna}", styles['BodyText']))
    story.append(Image(nome_arquivo, width=400, height=300))
    story.append(Spacer(1, 12))

# Adicionar resumo final explicativo
story.append(PageBreak())
story.append(Paragraph("📌 Resumo das principais causas do Churn", styles['Heading2']))

resumo_texto = (
    "Com base nas análises realizadas, destacam-se alguns fatores importantes que influenciam a saída dos clientes:\n\n"
    + "\n".join(f"- {explicacao}" for explicacao in explicacoes) + 
    "\n\nEstes resultados indicam que ações focadas em melhorar os aspectos associados a essas variáveis podem ajudar a reduzir o churn e aumentar a retenção."
)
story.append(Paragraph(resumo_texto.replace("\n", "<br />"), styles['BodyText']))

# Finalizar e salvar o PDF
doc.build(story)

# Limpar imagens temporárias
for arquivo in os.listdir():
    if arquivo.endswith(".png"):
        os.remove(arquivo)

print(f"✅ Relatório gerado com sucesso em: {pdf_path}")

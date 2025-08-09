## TelecomX - Pipeline de Extração e Carga (ETL)

Este projeto realiza a extração do dataset TelecomX em JSON, normaliza os dados (flatten) em colunas tabulares e carrega no SQLite para análises.

### Estrutura do Projeto
- `api/TelecomX_Data.json`: fonte de dados em JSON (ou `api/TelecomX_data.json`).
- `api/extraction.py`: inspeção e exploração do JSON (dimensões, tipos, preview, chaves aninhadas).
- `api/data_base_load.py`: normalização (flatten) e carga dos dados para SQLite.
- `api/telecomx.db`: banco SQLite gerado com a tabela `telecomx_dados`.
- `api/TelecomX_dicionario.md`: dicionário de dados (se aplicável).

### Pré-requisitos
- Python 3.10+
- Pip

### Ambiente Virtual (recomendado)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas
```

### Execução
1) Inspecionar dados (opcional):
```bash
python api/extraction.py
```

2) Normalizar e carregar em SQLite:
```bash
python api/data_base_load.py
```

Saída esperada na execução de carga:
- Preview do DataFrame (head)
- Dimensões e lista de colunas
- Banco gerado em `api/telecomx.db` com a tabela `telecomx_dados`

### Como funciona a normalização (flatten)
A partir de um registro exemplo:
```json
{
  "customerID": "9812-GHVRI",
  "Churn": "No",
  "customer": {"gender": "Female", "SeniorCitizen": 0, "Partner": "No", "Dependents": "No", "tenure": 40},
  "phone": {"PhoneService": "Yes", "MultipleLines": "Yes"},
  "internet": {"InternetService": "Fiber optic", "OnlineSecurity": "No", "OnlineBackup": "No", "DeviceProtection": "No", "TechSupport": "No", "StreamingTV": "No", "StreamingMovies": "Yes"},
  "account": {"Contract": "Month-to-month", "PaperlessBilling": "No", "PaymentMethod": "Bank transfer (automatic)", "Charges": {"Monthly": 83.85, "Total": "3532.25"}}
}
```
O processo gera colunas como:
- `customerID`, `Churn`
- `customer.gender`, `customer.SeniorCitizen`, `customer.Partner`, `customer.Dependents`, `customer.tenure`
- `phone.PhoneService`, `phone.MultipleLines`
- `internet.InternetService`, `internet.OnlineSecurity`, `internet.OnlineBackup`, `internet.DeviceProtection`, `internet.TechSupport`, `internet.StreamingTV`, `internet.StreamingMovies`
- `account.Contract`, `account.PaperlessBilling`, `account.PaymentMethod`, `account.Charges.Monthly`, `account.Charges.Total`

### Banco de Dados
- Caminho: `api/telecomx.db`
- Tabela: `telecomx_dados`
- Tipos: colunas criadas como `TEXT` por simplicidade; números são armazenados como texto. Se desejar tipagem numérica, adapte a criação de tabela e conversões.

Exemplo de consulta rápida:
```python
import sqlite3
conn = sqlite3.connect('api/telecomx.db')
cur = conn.cursor()
cur.execute('SELECT COUNT(*) FROM telecomx_dados')
print('Linhas:', cur.fetchone()[0])
conn.close()
```

### Solução de Problemas
- Erro ao instalar pacotes (PEP 668): use ambiente virtual (`python3 -m venv .venv`).
- JSON não encontrado: verifique nomes `TelecomX_Data.json` vs `TelecomX_data.json` e pasta `api/`.
- Colunas ausentes: execute novamente a carga com a opção padrão que recria a tabela.

### Licença
Uso educacional/demonstrativo. Ajuste conforme necessário.

### Autor
- Nome: Chris
- GitHub: https://github.com/chris
- Bio: Cientista de Dados / Eng. de Dados focado em ETL, análise de churn e modelagem.
- Contato: chris@example.com
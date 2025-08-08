# telecomx_1
Link da API:
https://github.com/ingridcristh/challenge2-data-science/blob/main/TelecomX_Data.json
https://github.com/ingridcristh/challenge2-data-science/tree/main


![alt text](image.png)

Motivos do churn segundo as variáveis apresentadas:
Tempo de cliente (customer_tenure):

![alt text](image-1.png)

Clientes que saíram (Churn = Yes) têm em média menor tempo de permanência (aprox. 18 meses) comparado aos que ficaram (aprox. 38 meses).

![alt text](image-4.png)

Correlação negativa moderada (-0.34) indica que quanto menor o tempo de cliente, maior a chance de churn.

Ou seja, clientes novos tendem a sair mais rápido.


Valor da cobrança mensal (account_Charges_Monthly):

![alt text](image-5.png)

Clientes que saíram pagam em média mais caro por mês (74,44) que os que ficaram (61,27).

Correlação positiva (0.19) sugere que clientes com cobranças mensais mais altas têm maior probabilidade de cancelar.

Isso pode indicar insatisfação com custo-benefício, levando à saída.

Idade (indicador customer_SeniorCitizen):

![alt text](image-3.png)

Clientes que saíram têm maior proporção de idosos (25%) do que os que ficaram (13%).

Correlação positiva (0.15) mostra que clientes idosos têm uma leve tendência a churn maior.

Talvez por necessidades diferentes ou menos engajamento com os serviços.

Resumo final
O churn está acontecendo principalmente porque:

Clientes novos (baixo tempo de contrato) têm maior risco de sair; talvez por falta de fidelização ou adaptação ao serviço.

Clientes que pagam mensalidades mais altas parecem mais propensos a cancelar, sugerindo que preço ou percepção de valor podem ser um problema.

Clientes idosos também apresentam maior tendência a cancelar, o que pode requerer atenção específica no atendimento ou oferta de serviços.

Recomendações iniciais
Investir em programas de fidelização e onboarding para clientes novos.

Revisar estratégias de preço ou pacotes para clientes com cobranças altas.

Oferecer suporte personalizado para clientes idosos.


Analises;

Colunas numéricas: ['customer_SeniorCitizen', 'customer_tenure', 'account_Charges_Monthly']
🔤 Colunas categóricas: ['customerID', 'customer_gender', 'customer_Partner', 'customer_Dependents', 'phone_PhoneService', 'phone_MultipleLines', 'internet_InternetService', 'internet_OnlineSecurity', 'internet_OnlineBackup', 'internet_DeviceProtection', 'internet_TechSupport', 'internet_StreamingTV', 'internet_StreamingMovies', 'account_Contract', 'account_PaperlessBilling', 'account_PaymentMethod', 'account_Charges_Total']

📊 Distribuição da variável 'Churn':
Churn
No     0.73463
Yes    0.26537
Name: proportion, dtype: float64

📈 Estatísticas das variáveis numéricas por 'Churn':
       customer_SeniorCitizen  customer_tenure  account_Charges_Monthly
Churn                                                                  
No                   0.128721        37.569965                61.265124
Yes                  0.254682        17.979133                74.441332

🔗 Correlação com 'Churn':
Churn                      1.000000
account_Charges_Monthly    0.189866
customer_SeniorCitizen     0.146733
customer_tenure           -0.344079
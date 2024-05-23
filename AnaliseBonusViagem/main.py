import pandas as pd
from twilio.rest import Client

account_sid = "account_sid"
auth_token  = "token"
client = Client(account_sid, auth_token)

# Passo a passo de solução 
# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Para cada arquivo:
# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor.

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="number",
            from_="+13345649773",
            body=f'No mes {mes}, Alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)


# Caso não seja maior do que 55.000, não quero fazer nada.
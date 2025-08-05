import pandas as pd
from pathlib import Path

DATASET_PATH = Path(__file__).parent.parent
DATASET_FILE = DATASET_PATH / 'datasets/vendas_funcs.xlsx'

dataset = pd.read_excel(DATASET_FILE)

# Cabeçalho da tabela
cabecalho = f"{'NOME':<12} | {'ESTADO':<20} | {'VENDAS':>10}"
separador = "-" * len(cabecalho)

# Vendedores com vendas acima de R$18.000
print("Vendedores com vendas acima de R$18.000:\n")
print(cabecalho)
print(separador)

vendedores_acima_18000 = dataset[dataset['Vendas'] > 18000]

for _, row in vendedores_acima_18000.iterrows():
    print(f"{row['Nome']:<12} | {row['Estado']:<20} | R${row['Vendas']:>8}")
print(separador)

# Vendedores do RIO DE JANEIRO
print("\nVendedores do RIO DE JANEIRO:\n")
print(cabecalho)
print(separador)

vendedores_rj = dataset[dataset['Estado'] == 'RIO DE JANEIRO']

for _, row in vendedores_rj.iterrows():
    print(f"{row['Nome']:<12} | {row['Estado']:<20} | R${row['Vendas']:>8}")
print(separador)

# Vendedores de SAO PAULO com vendas acima de R$14.000
print("\nVendedores de SAO PAULO com vendas acima de R$14000\n")
print(cabecalho)
print(separador)

vendedores_sp_vendas_maior_que_14000 = dataset.query('Estado == "SAO PAULO" & Vendas > 14000')

for _, row in vendedores_sp_vendas_maior_que_14000.iterrows():
    print(f"{row['Nome']:<12} | {row['Estado']:<20} | R${row['Vendas']:>8}")
print(separador)
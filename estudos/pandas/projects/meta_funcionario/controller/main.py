import pandas as pd
from pathlib import Path

DATASET_PATH = Path(__file__).parent.parent
DATASET_FILE = DATASET_PATH / 'datasets/vendas_funcs.xlsx'

dataset = pd.read_excel(DATASET_FILE)

print('Bateram a meta:')
for i in range(len(dataset)):
    if dataset.loc[i, 'Vendas'] > 18000:
        print(f'Nome: {dataset.loc[i, "Nome"]} - Vendas: {dataset.loc[i, "Vendas"]}')

print('\nVendas abaixo do mínimo:')
for i in range(len(dataset)):
    if dataset.loc[i, 'Vendas'] < 7000:
        print(f'Nome: {dataset.loc[i, "Nome"]} - Vendas: {dataset.loc[i, "Vendas"]}')

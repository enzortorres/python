import pandas as pd
import numpy as np
import random as rd
from pathlib import Path

DATASET_PATH = Path(__file__).parent.parent
DATASET_FILE = DATASET_PATH / 'datasets/vendas_funcs.xlsx'

ESTADOS_BRASIL = [
    "ACRE", "ALAGOAS", "AMAPA", "AMAZONAS", "BAHIA", "CEARA",
    "DISTRITO FEDERAL", "ESPIRITO SANTO", "GOIAS", "MARANHAO",
    "MATO GROSSO", "MATO GROSSO DO SUL", "MINAS GERAIS", "PARA",
    "PARAIBA", "PARANA", "PERNAMBUCO", "PIAUI", "RIO DE JANEIRO",
    "RIO GRANDE DO NORTE", "RIO GRANDE DO SUL", "RONDONIA",
    "RORAIMA", "SANTA CATARINA", "SAO PAULO", "SERGIPE", "TOCANTINS"
]

nomes = [f'Pessoa {i+1}' for i in range(100)]
estados = rd.choices(ESTADOS_BRASIL, k=100)
vendas = np.random.randint(5000, 20001, size=100)

df = pd.DataFrame({
    'Nome': nomes,
    'Estado': estados,
    'Vendas': vendas,
})

df.to_excel(DATASET_FILE, index=False)
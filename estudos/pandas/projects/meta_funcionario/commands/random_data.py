import pandas as pd
import numpy as np
from pathlib import Path

DATASET_PATH = Path(__file__).parent.parent
DATASET_FILE = DATASET_PATH / 'datasets/vendas_funcs.xlsx'

nomes = [f'Pessoa {i+1}' for i in range(100)]   
vendas = np.random.randint(5000, 20001, size=100)

df = pd.DataFrame({
    'Nome': nomes,
    'Vendas': vendas
})

df.to_excel(DATASET_FILE, index=False)
import pandas as pd

data = pd.read_csv("titanic_train.csv")

# > 5 primeiras linhas
# print(data.head())

# > 5 últimas linhas
# print(data.tail())

# > Número de linhas e colunas
# print(data.shape)
# print(f"{data.shape[0]} linhas.")
# print(f"{data.shape[1]} colunas.")

# > Tipos dos dados
# print(data.dtypes)

# > Tipos de dados e valores vazios (null)
# print(data.info())

# > Contar valores vazios por coluna
print(data.isnull().sum())
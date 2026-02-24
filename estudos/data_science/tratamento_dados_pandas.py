import pandas as pd

data = pd.read_csv('titanic_train.csv')

# > Verificando as informações da base
# print(data.info())

# > Eliminando a coluna 'Cabin'
data = data.drop('Cabin', axis=1)

# > Verificando se foi removido
# print(data.info())

# > Eliminar linhas com valores vazios
data.dropna(inplace=True) 

# > Selecionando as colunas com o tipo "object"
objects_data = data.dtypes[data.dtypes.values == 'object'].index

# > Eliminando essas colunas
data = data.drop(objects_data, axis=1)

print(data.info())
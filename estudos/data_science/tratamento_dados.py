import pandas as pd

data = pd.read_csv('titanic_test.csv')

# > Retirando colunas com alta cardinalidade.
data = data.drop(['PassengerId', 'Name'], axis=1)

# > Eliminando a coluna Cabin pela alta cardinalidade e quantidade de valores vazios.
data = data.drop('Cabin', axis=1)

# > Ao invés de apagar as linhas onde idade é vazio, vamos substituir esses valores pela média das idades
media_idade = data['Age'].mean()

data.loc[data.Age.isnull(), 'Age'] = media_idade # > Atribuindo a média a todas as `Idades` que estão com valores vazios.

# > Novamente elminando os dados do tipo objeto
colunas = data.dtypes[data.dtypes.values == 'object'].index
data = data.drop(colunas, axis=1)

print(data.info())
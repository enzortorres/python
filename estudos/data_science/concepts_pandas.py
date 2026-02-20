import pandas as pd

data = pd.read_csv("titanic_train.csv")

# | Visualizar informações da base

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
# print(data.isnull().sum())

dados = {
    "X": [1,2,3,6,8,23]
}

dados = pd.DataFrame(dados)

# > Média dos valores de um array
# print(dados.mean())

# > Mostrando a contagem de registros
# print(dados.count())

# > Mediana
# print(dados.median())

# > Desvio padrão (O quanto esses dados estão variando da média)
# print(dados.std())

# > Trazendo todo o resumo estatístico utilizando describe
# print(dados.describe())
# print(data.describe())

# | Escolhendo colunas da base

# > Podemos usar o nome da coluna entre aspas (Pode usar espaço)
# print(data['Survived'])

# > Ou usar ponto (Não pode usar espaço)
# print(data.Survived)

# > Usando uma coluna, podemos contar a quantidade de vezes que cada valor aparece
# print(data.Survived.value_counts())

# > Selecionar mais de uma coluna
# print(data[['Survived', 'Sex', 'Age']])

# > Verificando clientes que pagaram mais de 100 libras
# print(data[data.Fare > 100])

# > Verificando se tiveram clientes que pagaram menos de 5 libras
# print(data[data.Fare < 5])

# > Também conseguimos usar operadores lógicos
# print(data[(data.Parch > 1) | (data.SibSp > 1)])

# > Uma forma muito útil de fazer seleção de dados é usando o .loc() ou o .iloc()
# print(data.loc[(data.Parch > 1) & (data.SibSp > 1)].head())

# > Ele permite filtras colunas de forma muito prática
# print(data.loc[(data.Parch > 1) & (data.SibSp > 1), ['PassengerId', 'Parch', 'SibSp']].head())

# print(data.loc[
#     (data.Parch > 1) & (data.SibSp > 1), # where
#     ['PassengerId', 'Parch', 'SibSp'] # colunas
# ].head())

# > Já o .iloc() vai usar o índice para filtrar
# print(data.iloc[30:40])

# > Também posso usar para buscar apenas colunas específicas
# print(data.iloc[
#     30:40, # linhas
#     3:6 # colunas (Name, Sex, Age)
# ])

# | Podemos fazer gráficos com Pandas de forma bem simples
import matplotlib.pyplot as plt

# > É possível fazer um histograma simples
# data.Fare.hist(bins=100) # ? bin?s são como se fosse o intervalo, definir muitos bins mostram detalhes finos, mas podendo dificultar a visualização, poucos bins resume muito os dados, podendo esconder padrões importantes

# > Gráfico de barras
# data.Pclass.plot.bar() # ? muitos dados, pois ta fazendo um gráfico de cada linha de `Pclass`
# data.Pclass.value_counts().plot.bar() # ? Gráfico com a contagem de cada valor de `Pclass`

# > E até gráfico mais complexos como o de densidade
# data['Fare'].plot.kde()

"""
· Survived: sobrevivente (0 = Não, 1 = Sim)
. Pclass: Classe da passagem (1 = primeira classe, 2 = segunda classe, 3 = terceira classe)
· Name: nome do passageiro
· Sex: Gênero do passageiro
· Age: Idade (em anos) do passageiro
· SibSp: número de irmãos / cônjuges a bordo do Titanic
· Parch: número de pais / filhos a bordo do Titanic
· Ticket: número do ticket
· Fare: tarifa da passagem
· Cabin: número da cabine
· Embarked: porto de embarque (C = Cherbourg, Q = Queenstown, S = Southampton)

As colunas desse dataset são:
· Passenger ID: ID do passageiro (número único para cada um dos passageiros)
"""

# plt.show() # Para exibir o gráfico 

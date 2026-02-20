import pandas as pd

data = pd.read_csv('titanic_train.csv')
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

# > Para ver as 3 primeiras linhas
# print(data.head(3))

# > Para ver a quantidade de números únicos
# print(data.nunique())

# | Visualizando de forma gráfica

# > Importando o matplotlib
import matplotlib.pyplot as plt

# > Verificando o histograma das tarifas
# : plot : 
# base = data[data.Fare < 100].Fare

# fig, ax = plt.subplots()

# ax.hist(base, bins=40, linewidth=0.5, edgecolor="white")

# > Verificando o boxplot para a coluna Fare
# : plot :
# base = data[data.Fare < 100].Fare

# fig, ax = plt.subplots()

# ax.boxplot(base)


# | Dependendo do visual, outras bibliotecas já podem ter opções mias prontas para usarmos, como o caso do pairplot no seaborn

# > Importando o seaborn
import seaborn as sns

# > Criando o pairplot
# sns.pairplot(data, hue='Survived')

# > Criando uma matriz de correlação entre as variáveis
# print(data.corr(numeric_only=True))

# > Utilizando o heatmap do seaborn para tornar essa matriz mais visual
sns.heatmap(data.corr(numeric_only=True))

# ! Importante para mostrar o gráfico
plt.show()
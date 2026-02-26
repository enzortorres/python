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

# ! Utilizando Scikit-Learn

print("\nDados de treino\n")

# > Definindo o X e o y para o treino
x = data.drop('Survived', axis=1)
y = data.Survived


# | Utilizando KNN
from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x, y)

# > Avaliando o modelo
print(neigh.score(x, y))

# | Utilizando Tree
from sklearn import tree
clf_tree = tree.DecisionTreeClassifier(random_state=0)
clf_tree = clf_tree.fit(x, y)

# > Avaliando o modelo
print(clf_tree.score(x,y))

# | Utilizando regressão logística

from sklearn.linear_model import LogisticRegression

clf_log = LogisticRegression(random_state=0, max_iter=1000).fit(x, y)
print(clf_log.score(x, y))

data_test = pd.read_csv("titanic_test.csv")

# ! Fazendo os mesmos tratamento para os dados de teste

print("\nDados de teste\n")

# > Eliminar a coluna `Cabin`
data_test = data_test.drop('Cabin', axis=1)

# > Eliminar linhas com valores vazios
data_test.dropna(inplace=True) 

# > Selecionando as colunas com o tipo `object`
objects_data = data_test.dtypes[data_test.dtypes.values == 'object'].index

# > Eliminando essas colunas
data_test = data_test.drop(objects_data, axis=1) 

# > Separando X e y da base de teste
x_test = data_test.drop('Survived', axis=1)
y_test = data_test.Survived

neigh_test = KNeighborsClassifier(n_neighbors=3)

# > Fazendo a predição com o KNN
pred_KNN = neigh.predict(x_test)
print(neigh.score(x, y))

# > Predict com a Árvore de Decisão
pred_Tree = clf_tree.predict(x_test)
print(clf_tree.score(x,y))

# > Predict com Regressão Logística
pred_Log = clf_log.predict(x_test)
print(clf_log.score(x, y))





# | Usando matriz de confusão
# url: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

print("\nMatriz de Confusão\n")

# > Importando a matriz de confusão
from sklearn.metrics import confusion_matrix

# > Verificando a matriz para o KNN
print("KNN")
print(confusion_matrix(y_test, pred_KNN))

print("TREE")
# > Verificando a matriz para a Árvore
print(confusion_matrix(y_test, pred_Tree))

print("LOG")
# > Verificando a matriz para a Regressão Logística
print(confusion_matrix(y_test, pred_Log))

# | Usando Acurácia
# url: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html

print("\nAcurácia\n")

# > Importando a métrica de acurácia
from sklearn.metrics import accuracy_score

# > Verificando a acurácia para o KNN
print("KNN")
print(accuracy_score(y_test, pred_KNN))

print("TREE")
# > Verificando a acurácia para a Árvore
print(accuracy_score(y_test, pred_Tree))

print("LOG")
# > Verificando a acurácia para a Regressão Logística
print(accuracy_score(y_test, pred_Log))

# | Usando Precisão

print("\nPrecisão\n")

# > Importando a métrica de precisão
from sklearn.metrics import precision_score

# > Verificando a precisão para o KNN
print("KNN")
print(precision_score(y_test, pred_KNN))

print("TREE")
# > Verificando a precisão para a Árvore
print(precision_score(y_test, pred_Tree))

print("LOG")
# > Verificando a precisão para a Regressão Logística
print(precision_score(y_test, pred_Log))

# | Usando o Recall
# url: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html

print("\nRecall\n")

# > Importando a métrica do recall
from sklearn.metrics import recall_score

# > Verificando o recall para o KNN
print("KNN")
print(recall_score(y_test, pred_KNN))

print("TREE")
# > Verificando o recall para a Árvore
print(recall_score(y_test, pred_Tree))

print("LOG")
# > Verificando o recall para a Regressão Logística
print(recall_score(y_test, pred_Log))

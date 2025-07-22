import pandas as pd

data = pd.read_csv('C:\\Users\\enzor\\OneDrive\\Desktop\\Estudos\\python\\estudos\\pandas\\datasets\\2004-2021.csv', sep=";")
print(data)

data.info()

df = pd.DataFrame({
    'nome': ['Enzo', 'Vitor'],
    'idade': [20, 20]
})

print(df)
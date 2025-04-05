import json

pessoa = {
    'nome': 'Enzo',
    'sobrenome': 'Ribas Torres',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

caminho_arquivo = 'C:\\Users\\enzor\\OneDrive\\Desktop\\Estudos\\python\\estudos\\curso_udemy\\fundamentos\\json\\'
file_name = caminho_arquivo + 'main.json'

with open(file_name, 'w', encoding="UTF-8") as file:
    json.dump(
        pessoa,
        file,
        ensure_ascii=False, # > ensure_ascii para não salvar os caracteres especiais em ASCII e utilizar a codificação do sistema
        indent=4
    ) 

with open(file_name, 'r', encoding="UTF-8") as file:
    pessoa = json.load(file) # > Para puxar os dados do json para uma variável, retorna um dicionário
    for key, value in pessoa.items():
        print(f"{key}: {value}")
    
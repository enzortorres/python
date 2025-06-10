from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = BASE_DIR / 'main.json'

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

if __name__ == '__main__':
    data_nome = input("Digite o seu nome: ")
    data_idade = int(input("Digite a sua idade: "))
    data_altura = float(input("Digite a sua altura em metros(m): "))

    person_data = Pessoa(data_nome, data_idade, data_altura)

    with open(FILE_NAME, "w", encoding='UTF-8') as file:
        json.dump(
            person_data.__dict__,
            file,
            ensure_ascii=False,
            indent=4,
        )

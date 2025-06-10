from register import FILE_NAME, Pessoa
import json

with open(FILE_NAME, 'r', encoding='UTF-8') as file:
    person_data = json.load(file)
    person = Pessoa(**person_data)

print(person.__dict__)
    
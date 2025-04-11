import sqlite3
from pathlib import Path

PATH_FILE = Path(__file__).parent
DB_NAME = 'db_teste.sqlite3'
DB_PATH = PATH_FILE / DB_NAME

connection = sqlite3.connect(DB_PATH)

cursor = connection.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS users ( '
    '   id INT NOT NULL PRIMARY KEY, '
    '   nome TEXT '
    ')'
)
connection.commit()

id = int(input("Digite o id do usuário: "))
nome = input("Digite o nome do usuário: ")

sql = (
    'INSERT INTO users (id, nome) VALUES '
    '(?, ?) '
)

data = (id, nome)
try:
    cursor.execute(sql, data)
except sqlite3.IntegrityError:
    raise sqlite3.IntegrityError("ID já cadastrado.")

connection.commit()

cursor.close()
connection.close()
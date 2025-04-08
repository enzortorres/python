import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)


# cursor.fetchall() # > Retorna o valor das linhas em uma lista

for row in cursor.fetchall(): # > Retorna cada linha para variável temporária "row"
    # _id = row[0] 
    # name = row[1]
    # weight = row[2] # ? Mesma coisa que o método de baixo
    _id, name, weight = row # > Desempacota os valores (id, name, weight) da linha
    print(_id, name, weight)

print()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
    '   WHERE id = "3"' 
)

row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()
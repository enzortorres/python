import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent # > Para pegar o endereço da pasta atuals
DB_NAME = 'db.sqlite3' # > Nome do arquivo 
DB_FILE = ROOT_DIR / DB_NAME # > Caminho do arquivo
TABLE_NAME = 'customer' # > Nome da tabela

connection = sqlite3.connect(DB_FILE) # > Para conectar/criar arquivo sqlite
cursor = connection.cursor() # > Para criar o cursor

# > Para cria uma tabela
cursor.execute(
    f"""\
    CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL
    )
    """
)
connection.commit()

# sql = ( 
#     f'INSERT INTO {TABLE_NAME}'
#     '(name, weight) VALUES'
#     '(:nome, :peso)' # > Os nomes das chaves do dicionário
# )
# print(sql)

# cursor.execute(sql, {'nome': 'Matheus', 'peso': 10}) # > No caso de usar dicionários, os placeholders precisam ser o nome das chaves
# cursor.executemany(sql, (
#     {'nome': 'Joãozinho', 'peso': 3},
#     {'nome': 'Helena', 'peso': 2},
#     {'nome': 'Maria', 'peso': 4},
#     {'nome': 'Joaninha', 'peso': 5},
# ))
# connection.commit()

# # > Registrar valores nas colunas da tabela
# # ! CUIDADO: SQL Injection
# # cursor.execute(sql, ('Joana', 4)) 
# cursor.executemany(
#     sql,
#     (('Joana', 4), ('Enzo', 5))
# ) # > Melhor maneira de previnir SQL Injection
# connection.commit()

# > Registrar vários valores nas colunas da tabela

# # > Para atualizar uma tabela
# cursor.execute( 
#     f"""\
#     UPDATE {TABLE_NAME} 
#         SET name = 'Adriane'
#         WHERE id = 2
#     """
# )
# connection.commit()

# ! CUIDADO: Fazendo delete sem where
# > Apaga tudo do banco de dados, porém o ID por sem autoincremental, continua do último ID
# cursor.execute(
#     f"""
#     DELETE FROM {TABLE_NAME} 
#     """
# )
# connection.commit()

# > Para zerar a "sequência" do ID
# cursor.execute(
#     f"""\
#     DELETE FROM sqlite_sequence 
#         WHERE name="{TABLE_NAME}"
#     """
# )
# connection.commit()

# > Precisa fechar o cursor e a conexão ao final do código
cursor.close()
connection.close()

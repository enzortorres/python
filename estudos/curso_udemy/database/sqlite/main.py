import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent # > Para pegar o endereço da pasta atuals
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customer'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

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

# > Registrar valores nas colunas da tabela
# ! CUIDADO: SQL Injection
cursor.execute( 
    F"""\
    INSERT INTO {TABLE_NAME} (id, name, weight) VALUES
        (NULL, 'Enzo Ribas', 9.5),
        (NULL, 'Helena', 4)
    """
)
connection.commit()

# > Para atualizar uma tabela
cursor.execute( 
    f"""\
    UPDATE {TABLE_NAME} 
        SET name = 'Adriane'
        WHERE id = 2
    """
)
connection.commit()

# ! CUIDADO: Fazendo delete sem where
# > Apaga tudo do banco de dados, porém o ID por sem autoincremental, continua do último ID
cursor.execute(
    f"""
    DELETE FROM {TABLE_NAME} 
    """
)
connection.commit()

# > Para zerar a "sequência" do ID
cursor.execute(
    f"""
    DELETE FROM sqlite_sequence 
        WHERE name="{TABLE_NAME}
    """
)
connection.commit()


cursor.close()
connection.close()

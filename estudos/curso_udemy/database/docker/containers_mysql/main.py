# # | PyMySql - um cliente MySQL feito em Python puro
# > Doc: https://pymysql.readthedocs.io/en/latest/
# > Pypy: https://pypi.org/project/pymysql/
# > GitHub: https://github.com/PyMySQL/PyMySQL

# ! Importações necessárias
import pymysql # ? Precisa instalar a biblioteca pymysql com o pip
import pymysql.cursors

import dotenv
import os

dotenv.load_dotenv() # Para carregar os dados da .env, precisa estar na mesma pasta a ".env"

connection = pymysql.connect(
    # Puxa os dados pelas variavéis de ambiente do .env 
    host=os.environ['MYSQL_HOST'],
    database=os.environ['MYSQL_DATABASE'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    charset='utf8mb4', # Não precisa necessáriamente pois na configuração do servidor pelo docker-compose já está com o charset configurado
    cursorclass=pymysql.cursors.DictCursor,
)

# print(os.environ['MYSQL_DATABASE'])

TABLE_NAME = 'users'


with connection:
    # ! Manipulando valores com CREATE, INSERT, TRUNCATE
    with connection.cursor() as cursor:
        cursor.execute(
            # É bom deixar um espaço em branco ao final das linhas, para não ocorrer erros
            'CREATE TABLE IF NOT EXISTS users ( ' # CREATE não precisa de commit
            '   id INT NOT NULL AUTO_INCREMENT, '
            '   name VARCHAR(50) NOT NULL, '
            '   idade INT NOT NULL, '
            '   PRIMARY KEY (id) '
            ')'
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}') # ! CUIDADO: ISSO LIMPA A TABELA
        
    # Começo a manipular dados a partir daqui
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            '   VALUES (%s, %s) ' # ! Placeholders para prevenir SQL Injections
        )
        data_tuple = ('Enzo', 20)
        results = cursor.execute(sql, data_tuple)

    connection.commit() # As modificações não são autocomitadas, então é necessário comitar para salvar as modificações
    
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            '   VALUES (%(nome)s, %(idade)s) ' # Quando for usar placeholders com dicionário, precisa colocar o nome das chaves
        )
        data_dict = {
            'nome': 'Guilherme',
            'idade': 62,
        } 
        results = cursor.execute(sql, data_dict)
                
        cursor.execute(
            f'SELECT id FROM {TABLE_NAME} '
            '   ORDER BY id DESC LIMIT 1'
        ) 
        lastIdFromSelect = cursor.fetchone()
        
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            '   VALUES (%(nome)s, %(idade)s) ' # Quando for usar placeholders com iteráveis, no caso dicionários, precisa colocar o nome das chaves
        )
        data_dict_iterator = (
            {'nome': 'Patrick', 'idade': 23,},
            {'nome': 'Jesus', 'idade': 44,},
            {'nome': 'Delia', 'idade': 31,},
        )
        results = cursor.executemany(sql, data_dict_iterator)
        
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            '   VALUES (%s, %s) ' # Quando for usar placeholders com iteráveis, no caso tuplas, precisa colocar por posição
        )
        data_tuple_iterator = (
            ('Siri', 23),
            ('Cortana', 63),
        )
        results = cursor.executemany(sql, data_tuple_iterator)

    # print(sql, data_tuple_iterator)
    # print(f"{results} linha(s) afetada(s).")
    connection.commit() # As modificações não são autocomitadas, então é necessário comitar para salvar as modificações
    
    # ! Lendo valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4
        
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            f'WHERE id >= %s  AND id <= %s ' # Desta forma está protegido de SQL Injection
        )
        
        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id))) # O que vai para o banco de dados
        
        # print(sql)
        # for row in cursor.fetchall(): # ? Desse jeito retorna um iterável, então só da para percorrer ele uma vez
        #     print(row)
            
        # data_select = cursor.fetchall() #  Retorna o iterável para a lista
        # for row in data_select: #  Desse jeito ele percorre uma lista
        #     print(row)
        
    # ! Lendo valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4
        
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            '   WHERE ID BETWEEN %s AND %s'
        )
        
        cursor.execute(sql, (menor_id, maior_id))
        # data_select = cursor.fetchall() #  Retorna o iterável para a lista
        
        # for row in data_select: #  Desse jeito ele percorre uma lista
        #     print(row)

    # ! DELETE SEM WHERE    
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
        )
        
        # cursor.execute(sql, (2,4))
        # connection.commit()

    # ! UPDATE SEM WHERE 
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            '   SET nome = "ENZO" '
        )
        
        # cursor.execute(sql)
        # connection.commit()
        
    # ! DELETE COM WHERE 
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            '   WHERE id = 4'
        )
        
        # print(cursor.execute(sql), "linha foi afetada.")
        connection.commit()
        
        # cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        
        # for row in cursor.fetchall():
        #     print(row)

    # ! UPDATE COM WHERE 
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            '   SET nome=%s, idade=%s'
            '   WHERE id = %s'
        )
        
        
        

        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            '   VALUES (%(nome)s, %(idade)s) ' # Quando for usar placeholders com iteráveis, no caso dicionários, precisa colocar o nome das chaves
        )
        data_dict_iterator = (
            {'nome': 'Patrick', 'idade': 23,},
            {'nome': 'Jesus', 'idade': 44,},
            {'nome': 'Delia', 'idade': 31,},
        )
        results = cursor.executemany(sql, data_dict_iterator)
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        data_cursor = cursor.fetchall()
    
        
        for row in data_cursor:
            print(row)
        
        print('resultsFromSelect', resultFromSelect)
        print('len(data_cursor)', len(data_cursor))
        print('rowcount', cursor.rowcount) # Retorna a quantidade de linhas afetadas pela última operação
        print('lastrowid na mão', lastIdFromSelect['id'])
        
        cursor.scroll(-2)
        print('rownumber', cursor.rownumber)

    connection.commit()

# cursor.close() # Utilizando "with" não precisa fechar manualmente
# connection.close() # Ao abrir uma conexão, precisa fecha-lá
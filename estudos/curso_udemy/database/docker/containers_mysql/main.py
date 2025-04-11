# # | PyMySql - um cliente MySQL feito em Python puro
# > Doc: https://pymysql.readthedocs.io/en/latest/
# > Pypy: https://pypi.org/project/pymysql/
# > GitHub: https://github.com/PyMySQL/PyMySQL

# ! Importações necessárias
import pymysql
import dotenv
import os

dotenv.load_dotenv() # Para carregar os dados da .env, precisa estar na mesma pasta a ".env"

connection = pymysql.connect(
    # Puxa os dados pelas variavéis de ambiente do .env 
    host=os.environ['MYSQL_HOST'],
    database=os.environ['MYSQL_DATABASE'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    charset='utf8mb4' # Não precisa necessáriamente pois na configuração do servidor pelo docker-compose já está com o charset configurado
)

# print(os.environ['MYSQL_DATABASE'])

TABLE_NAME = 'users'

with connection:
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

    print(sql, data_dict)
    connection.commit() # As modificações não são autocomitadas, então é necessário comitar para salvar as modificações
    # print(f"{results} linha(s) afetada(s).")
    
# cursor.close() # Utilizando "with" não precisa fechar manualmente
# connection.close() # Ao abrir uma conexão, precisa fecha-lá
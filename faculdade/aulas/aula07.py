from mysql import connector

TABLE_NAME = 'aluno'

connection = connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='aluno',
)

cursor = connection.cursor()

# # ? Criando a base de dados -------------------------------------------

# cursor.execute(
#     f'CREATE DATABASE IF NOT EXISTS {TABLE_NAME} '
# )

# cursor.execute(
#     'SHOW DATABASES '
# )
# for db in cursor:
#     print(db)

# # ? Usando o banco de dados ------------------------------------------- 

# cursor.execute(
#     'USE aula'
# )

# # ? Criar tabela aluno -------------------------------------------

# cursor.execute(
#     'CREATE TABLE IF NOT EXISTS aluno('
#     '   matricula INT PRIMARY KEY AUTO_INCREMENT, '
#     '   nome VARCHAR(30) NOT NULL, '
#     '   idade INT(3), '
#     '   email VARCHAR(40) '
#     ') '
# )

# # ? ? Mostrar todas as tabelas -------------------------------------------

# cursor.execute(
#     'SHOW TABLES'
# )
# for table in cursor:
#     print(table)

# # ? Mostar a descrição da tabela -------------------------------------------

# cursor.execute(
#     'DESC aluno'
# )
# for line in cursor:
#     print(line)

# # ? Inserir dados na tabela -------------------------------------------

# sql =  f'INSERT INTO aluno(nome, idade, email) ' \
#         '   VALUES("Enzo", 20, "teste@gmail.com") '

# cursor.execute(sql)
# connection.commit()
# print(f"{cursor.rowcount} linha(s) afetada(s).")

# # ? Inserindo dados por tabela

# lista = [
#     ("Natan", 20, "teste2@gmail.com"),
#     ("Guilherme", 19, "teste3@gmail.com"),
#     ("Marcelão", 26, "teste4@gmail.com"),
#     ("Pedro", 23, "teste5@gmail.com"),
#     ("Peu", 21, "teste6@gmail.com"),
# ]

# cursor.executemany(
#     'INSERT INTO aluno(nome, idade, email) ' \
#     '   VALUES (%s, %s, %s)',
#     lista
# )
# connection.commit()
# print(f"cursor.rowcount linha(s) afetada(s).")

# # ? Seleção simples

# cursor.execute('SELECT * FROM aluno ')

# query = cursor.fetchall()
# for linha in query:
#     print(linha)

# # ?

# cursor.execute(
#     'SELECT nome FROM aluno '
#     '   WHERE idade > 15 '
# )
# query = cursor.fetchall()
# for linha in query:
#     print(linha)

# # ? Ordenação asc/desc - order by

# print("\nOs nomes ordenados por nome (A-Z)\n")

# cursor.execute(
#     'SELECT nome FROM aluno '
#     '   ORDER BY nome ASC '
# )
# query = cursor.fetchall()
# for linha in query:
#     print(linha)

# print("\nOs nomes ordenados por nome (Z-A)\n")

# cursor.execute(
#     'SELECT nome FROM aluno '
#     '   ORDER BY nome DESC '
# )
# query = cursor.fetchall()
# for linha in query:
#     print(linha)
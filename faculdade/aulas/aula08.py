from mysql import connector

TABLE_NAME = 'aluno'

connection = connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='aluno',
)

cursor = connection.cursor()

# ? delete - deletar apenas 1 registro

# r = 'DELETE FROM aluno WHERE matricula in (%s, %s) '
# cursor.execute(r, (2,4))
# connection.commit()

# ? deletar mais de um valor

# r = 'DELETE FROM aluno WHERE matricula=1'
# cursor.execute(r)
# connection.commit()

# ? deletar com um intervalo

# r = 'DELETE FROM aluno' \
#     '   WHERE matricula BETWEEN (%s) AND (%s)'
# cursor.execute(r, (6,9))
# connection.commit()

# ? update - atualizar

# cursor.execute(
#     'UPDATE aluno '
#     '   SET nome="Tatiana Viana" '
#     '   WHERE matricula=3 '
# )
# connection.commit()
# print(cursor.rowcount, 'linha(s) alterada(s).')

# ? drop  - apaga tudo-------------------------------------------------------

# cursor.execute('drop database aula8')
# cursor.execute('drop table aluno')

cursor.close()
connection.close()
print('Conexão encerrada')
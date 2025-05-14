from mysql import connector
from tabulate import tabulate
from time import sleep

# ! 1 - Conexão e banco
try:
    connection = connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'sistema_escola',
    )
except:
    connection = connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = '',
    )

cursor = connection.cursor()

def criar_banco():
    cursor.execute('CREATE DATABASE IF NOT EXISTS sistema_escola ')

# ! 2 - Criação de Tabelas
def criacao_tabelas():
    cursor = connection.cursor()
    
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS turmas( 
                id INT PRIMARY KEY AUTO_INCREMENT,
                codigo VARCHAR(10),
                professor VARCHAR(100)
            ) 
        """
    )

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS alunos(  
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(100), 
                idade INT, 
                email VARCHAR(100), 
                turma_id INT, 
                FOREIGN KEY (turma_id) REFERENCES turmas(id) ON DELETE CASCADE
            )   
        """ 
    )
    

# ! 3 - Inserção de Dados
def inserir_dados():
    dados_turma = [
        ('SINA01', 'Thereza'),
        ('SINA02', 'João'),
        ('SINA03', 'Matheus'),
    ]

    cursor.executemany(
        """
            INSERT INTO turmas(codigo, professor) 
                VALUES (%s, %s)
        """,
        dados_turma
    )
    connection.commit()

    dados_alunos = [
        ('Enzo', 20, 'enzortorres@gmail.com', 1),
        ('Natan', 20, 'ntbz@gmail.com', 1),
        ('Marcelo', 26, 'marcelobourchardet@gmail.com', 2),
        ('Felipe', 31, 'feliperangel@gmail.com', 3),
        ('Guilherme', 19, 'guizadas@gmail.com', 1),
    ]

    cursor.executemany(
        """
            INSERT INTO alunos(nome, idade, email, turma_id) 
                VALUES (%s, %s, %s, %s)
        """,
        dados_alunos
    )
    connection.commit()

# ! 4 - Consultas

def consultas():
    headers = ['ID', 'Nome', 'Idade', 'Email', 'Turma ID']

    # > Liste todos os alunos com nome e turma
    cursor.execute('SELECT * FROM alunos')

    query = cursor.fetchall()

    print(tabulate(query, headers=headers, tablefmt='grid'))
    print(cursor.rowcount, 'linha(s) retornada(s).', end='\n\n')

    # > Mostre todos os alunos de uma turma específica
    search = (int(input("Digite o id da turma que deseja buscar: ")))

    sql  =  'SELECT * FROM alunos ' \
            '   WHERE turma_id = (%s) '
    cursor.execute(sql, (search,))
    query = cursor.fetchall()

    if cursor.rowcount:
        print(tabulate(query, headers=headers, tablefmt='grid'))
        print(cursor.rowcount, 'linha(s) retornada(s).', end='\n\n')
    else:
        print("\nTurma não encontrada ou não tem alunos na turma.\n")

    # > Liste todos os alunos com idade entre 13 e 15 anos (NÃO TEM)
    sql  =  'SELECT * FROM alunos ' \
            '   WHERE idade BETWEEN 13 AND 15'
    cursor.execute(sql)

    query = cursor.fetchall()
    if cursor.rowcount:
        print(tabulate(query, headers=headers, tablefmt='grid'))
    else:
        print("\nNenhum aluno com idade entre 13 e 15 anos.\n")

    # > Liste os professores e o total de alunos por turma
    sql  =  """
                SELECT turmas.professor, COUNT(alunos.id) FROM turmas
                    JOIN alunos ON turmas.id = alunos.turma_id
                    GROUP BY turmas.professor
            """
    cursor.execute(sql)

    headers = ['Professor', 'Total de alunos']

    query = cursor.fetchall()
    print(tabulate(query, headers=headers, tablefmt='grid'))


# ! 5 - Atualização
def atualizar_email():
    sql = """
        UPDATE alunos
            SET email = 'enzortorres2005@gmail.com'
            WHERE id = 1
    """
    cursor.execute(sql)
    connection.commit()

# ! 6 - Remoção
def remover():
    search_aluno = int(input("Digite um ID de um aluno para deletá-lo: "))
    sql = """
        DELETE FROM alunos
            WHERE id = (%s)
    """
    cursor.execute(sql, (search_aluno,))
    connection.commit()
    print(cursor.rowcount, "linha(s) afetada(s).")
        

    # > Ao remover uma turma, certifique-se de que os alunos associados também sejam removidos

    search_turma = int(input("Digite o ID de uma turma para deletá-la: "))
    sql = """
        DELETE FROM turmas
            WHERE id = (%s)
    """
    cursor.execute(sql, (search_turma,))
    connection.commit()
    print(cursor.rowcount, "linha(s) afetada(s).")

# ! 7 - Ordenação
def ordenacao():
    headers = ['ID', 'Nome', 'Idade', 'Email', 'Turma ID']

    sql = """
        SELECT * FROM alunos
            ORDER BY idade DESC
    """
    cursor.execute(sql)

    query = cursor.fetchall()

    print("\n\nTodos os alunos ordenados por idade decrescente")
    print(tabulate(query, headers=headers, tablefmt='grid'), "\n\n")

# ! 8 - Limpeza
def limpeza():
    sql = """
        DELETE FROM alunos
    """
    cursor.execute(sql)
    connection.commit()

    sql = """
        DELETE FROM turmas
    """
    cursor.execute(sql)
    connection.commit()

    sql = """
        DROP DATABASE sistema_escola
    """
    cursor.execute(sql)
    connection.commit()

comandos = {
    '1': criar_banco,
    '2': criacao_tabelas,
    '3': inserir_dados,
    '4': consultas,
    '5': atualizar_email,
    '6': remover,
    '7': ordenacao,
    '8': limpeza,
}

while True:
    comando = str(input(
        """Qual comando deseja realizar?
    1 - Criar o Banco
    2 - Criar as tabelas
    3 - Inserir dados
    4 - Consultas
    5 - Atualizar
    6 - Remoção
    7 - Ordenação
    8 - Limpeza
    9 - Sair
    >>> """
    ))
    try:
        comandos[comando]()
        print("\nComando realizado com sucesso!\n")
        sleep(1)
    except KeyError:
        print("Saindo do sistema...")
        break
    except Exception as error:
        print()
        print(f"\033[1;31m{error}\033[0m", end='\n\n')


cursor.close()
connection.close()
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database=''
)

cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS livraria')

cursor.execute('USE livraria')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente(
        codigo INT PRIMARY KEY AUTO_INCREMENT,
        endereco VARCHAR(30),
        CPF VARCHAR(14) NOT NULL,
        lista_livros VARCHAR(30)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoaFisica(
        codigo_cliente INT,
        FOREIGN KEY (codigo_cliente) REFERENCES cliente(codigo)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoaJuridica(
        codigo_cliente INT,
        FOREIGN KEY (codigo_cliente) REFERENCES cliente(codigo)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livro(
        nome_autor VARCHAR(30),
        assunto VARCHAR(30),
        editora VARCHAR(30),
        ISBN INT PRIMARY KEY AUTO_INCREMENT,
        qtd_estoque INT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS editora(
        codigo INT PRIMARY KEY AUTO_INCREMENT,
        endereco VARCHAR(30),
        telefone INT,
        nome_gerente VARCHAR(30)
    )
''')

dadosCliente = [
    ('20751022255', 'rua fagundes pinto', 'romance' ),
    ('16551012265', 'rua siqueira campos', 'terror' ),
    ('81171021235', 'rua ronaldo fagundes', 'ficção' )
]
# cursor.executemany('INSERT INTO cliente(CPF, endereco, lista_livros) VALUES(%s, %s, %s)', dadosCliente)

dadosLivros = [
    ('peppa', 'infantil', 'lasalle', 3),
    ('rocket league', 'Jovem', 'epic games', 18),
]
cursor.executemany('INSERT INTO livro(nome_autor, assunto, editora, qtd_estoque) VALUES(%s, %s, %s, %s)', dadosLivros)

cursor.execute("UPDATE cliente SET CPF='12351223123' WHERE codigo = 1")

connection.commit()

cursor.execute('SELECT qtd_estoque FROM livro')
for i in cursor:
    print(i)

cursor.execute('SELECT CPF FROM cliente')
for i in cursor:
    print(i)

cursor.execute('SELECT nome_autor FROM livro ORDER BY nome_autor DESC')
for i in cursor:
    print(i)

connection.close()
cursor.close()
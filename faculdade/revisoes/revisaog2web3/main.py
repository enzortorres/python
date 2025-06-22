from mysql import connector

from tkinter import *
from tkinter import messagebox

# > Conexão banco de dados

connection = connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='',
)

cursor = connection.cursor()

# > Banco de dados e tabelas

cursor.execute('CREATE DATABASE IF NOT EXISTS escola')

cursor.execute('USE escola')

cursor.execute(
    'CREATE TABLE IF NOT EXISTS alunos( '
    '   id_aluno INT PRIMARY KEY, '
    '   nome_aluno VARCHAR(50) NOT NULL, '
    '   email VARCHAR(100) UNIQUE NOT NULL, '
    '   telefone VARCHAR(20), '
    '   dt_nasc DATE '
    ') '
)

cursor.execute(
    'CREATE TABLE IF NOT EXISTS cursos( '
    '   id_curso INT PRIMARY KEY, '
    '   nome_curso VARCHAR(100) NOT NULL, '
    '   descricao TEXT '
    ') '
)

cursor.execute(
    'CREATE TABLE IF NOT EXISTS matriculas( '
    '   id_matricula INT PRIMARY KEY, '
    '   id_aluno INT NOT NULL, '
    '   id_curso INT NOT NULL, '
    '   dt_matricula DATE NOT NULL, '
    '   FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno), '
    '   FOREIGN KEY (id_curso) REFERENCES cursos(id_curso) '
    ') '
)

# > Interface

tk = Tk()
tk.geometry('500x300')
tk.title('Revisão G2 - Sistema escolar')

frame_aluno = Frame(tk)
frame_aluno.grid(row=0, column=1, sticky='nw', padx=50)


Label(frame_aluno, text='Aluno', font='Bold 16').grid(row=0, column=0)

Label(frame_aluno, text='Código').grid(row=1, column=0)
aluno_codigo = Entry(frame_aluno).grid(row=2, column=0)

Label(frame_aluno, text='Nome').grid(row=1, column=0)
aluno_nome = Entry(frame_aluno).grid(row=2, column=0)

Label(frame_aluno, text='Email').grid(row=3, column=0)
aluno_email = Entry(frame_aluno).grid(row=4, column=0)

Label(frame_aluno, text='Telefone').grid(row=5, column=0)
aluo_telefone = Entry(frame_aluno).grid(row=6, column=0)

Label(frame_aluno, text='Data de nascimento').grid(row=7, column=0)
aluno_dt_nascimento = Entry(frame_aluno).grid(row=8, column=0)

frame_curso = Frame(tk)
frame_curso.grid(row=0, column=2, sticky='ne', padx=50)

Label(frame_curso, text='Curso', font='Bold 16').grid(row=0, column=0)

Label(frame_curso, text='Código').grid(row=1,column=0)
curso_id_curso = Entry(frame_curso).grid(row=2, column=0)

Label(frame_curso, text='Nome').grid(row=3,column=0)
curso_nome = Entry(frame_curso).grid(row=4, column=0)

Label(frame_curso, text='Descrição').grid(row=5, column=0)
curso_desc = Entry(frame_curso).grid(row=6, column=0)




tk.mainloop()
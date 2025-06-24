from mysql import connector

from tkinter import *
from tkinter import messagebox

import datetime

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
    '   id_aluno INT AUTO_INCREMENT PRIMARY KEY, '
    '   nome_aluno VARCHAR(50) NOT NULL, '
    '   email VARCHAR(100) UNIQUE NOT NULL, '
    '   telefone VARCHAR(20), '
    '   dt_nasc DATE, '
    '   idade INT NOT NULL, '
    '   status VARCHAR(50) NOT NULL'
    ') '
)

cursor.execute(
    'CREATE TABLE IF NOT EXISTS cursos( '
    '   id_curso INT AUTO_INCREMENT PRIMARY KEY, '
    '   nome_curso VARCHAR(100) NOT NULL, '
    '   descricao TEXT '
    ') '
)

cursor.execute(
    'CREATE TABLE IF NOT EXISTS matriculas( '
    '   id_matricula INT AUTO_INCREMENT PRIMARY KEY, '
    '   id_aluno INT NOT NULL, '
    '   id_curso INT NOT NULL, '
    '   dt_matricula DATE DEFAULT CURRENT_DATE, '
    '   FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno), '
    '   FOREIGN KEY (id_curso) REFERENCES cursos(id_curso) '
    ') '
)

# > Funções aluno

def cadastrar_aluno():
    nome = aluno_nome.get()
    email = aluno_email.get()
    telefone = aluno_telefone.get()
    dt_nascimento = aluno_dt_nascimento.get()
    idade = aluno_idade.get()
    status = aluno_status.get()
    
    if nome == '' or email == '' or telefone == '' or dt_nascimento == '' or idade == '' or status == '':
        messagebox.showerror('Atualizar', 'Todos os campos são obrigatórios')
        return
    
    try:
        datetime.datetime.strptime(dt_nascimento, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror('Erro', 'Data de nascimento inválida. Use o formato YYYY-MM-DD.')
        return
    
    if status != 'Aprovado' and status != 'Reprovado' and status != 'Cursando':
        messagebox.showerror('Erro', 'Situação inválida')
        return
    
    try:
        cursor.execute(
            'INSERT INTO alunos(nome_aluno, email, telefone, dt_nasc, idade, status) '
            '   VALUES(%s, %s, %s, %s, %s, %s)', (nome, email, telefone, dt_nascimento, idade, status)
        )
        connection.commit()
        messagebox.showinfo('Sucesso', f'Aluno {nome} foi cadastrado(a) com sucesso!')
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao tentar cadastrar aluno!\n{e}')
    finally:
        aluno_codigo.delete(0, END)
        aluno_nome.delete(0, END)
        aluno_email.delete(0, END)
        aluno_telefone.delete(0, END)
        aluno_dt_nascimento.delete(0, END)
        aluno_idade.delete(0, END)

def visualizar_aluno():
    codigo = aluno_codigo.get()
    
    if codigo == '':
        messagebox.showerror('Atualizar', 'O campo "Código" é obrigatório!')
        return
    
    cursor.execute(
        'SELECT * FROM alunos'
        '   WHERE id_aluno=%s',
        (codigo,)
    )
    rows = cursor.fetchall()
    
    if rows:
        for row in rows:
            messagebox.showinfo('Visualizar', f'Código: {row[0]}\nNome: {row[1]}\nEmail: {row[2]}\nTelefone: {row[3]}\nData nascimento: {row[4]}\nIdade: {row[5]}\nStatus: {row[6]}')
    else:
        messagebox.showerror('Erro', 'Nenhum aluno encontrado!') 

def excluir_aluno():
    codigo = aluno_codigo.get()
    
    if codigo == '':
        messagebox.showerror('Atualizar', 'Informe o código do aluno para excluir')
        return

    try:
        cursor.execute(
            'DELETE FROM alunos '
            '   WHERE id_aluno=%s' ,
            (codigo,)
        )
        connection.commit()
        messagebox.showinfo('Excluir', 'Produto excluido com sucesso!')
        aluno_codigo.delete(0, END)
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao excluir aluno: {e}')

def trocar_status_aluno():
    codigo = aluno_codigo.get()
    status = aluno_status.get()
    
    if codigo == '':
        messagebox.showerror('Erro', 'Informe o código do aluno para trocar a situação do mesmo.')
        return
    
    if status != 'Aprovado' and status != 'Reprovado' and status != 'Cursando':
        messagebox.showerror('Erro', 'Situação inválida')
        return
    
    try:
        cursor.execute(
            'UPDATE alunos '
            '   SET status=%s'
            '   WHERE id_aluno=%s',
            (status, codigo,)
        )
        connection.commit()
        messagebox.showinfo('Sucesso', 'Situação atualizada')
    except Exception as e:
        messagebox.showerror('Erro', 'Erro ao tentar atualizar o status')    

def maiores_18_anos():
    try:
        cursor.execute(
            'SELECT * FROM alunos '
            '   WHERE idade >= 18'
        )
        
        rows = cursor.fetchall()
    
        if rows:
            nomes = ''
            for row in rows:
                nomes += f"{row[1]}\n"
        messagebox.showinfo('Maiores de 18', f'Alunos com mais de 18 anos:\n{nomes}')
    except Exception as e:
        messagebox.showerror('Erro', 'Erro ao procurar alunos maiores de 18 anos')

# > Funções curso

def cadastrar_curso():
    codigo = curso_codigo.get()
    nome = curso_nome.get()
    desc = curso_desc.get()
    
    if codigo == '' or nome == '' or desc == '':
        messagebox.showerror('Atualizar', 'Todos os campos são obrigatórios')
        return
    
    try:
        cursor.execute(
            'INSERT INTO cursos(id_curso, nome_curso, desc) '
            '   VALUES(%s, %s, %s)', (codigo, nome, desc)
        )
        connection.commit()
        messagebox.showinfo('Sucesso', f'Curso {nome} foi cadastrado(a) com sucesso!')
        curso_codigo.delete(0, END)
        curso_nome.delete(0, END)
        curso_desc.delete(0, END)
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao tentar cadastrar curso!\n{e}')

def visualizar_curso():
    codigo = curso_codigo.get()
    
    if codigo == '':
        messagebox.showerror('Atualizar', 'O campo "Código" é obrigatório!')
        return
    
    cursor.execute(
        'SELECT * FROM cursos'
        '   WHERE id_curso=%s',
        (codigo,)
    )
    rows = cursor.fetchall()
    
    if rows:
        for row in rows:
            messagebox.showinfo('Visualizar', f'Código: {row[0]}\nNome: {row[1]}\nDescrição: {row[2]}')
    else:
        messagebox.showerror('Erro', 'Nenhum curso encontrado!') 

def excluir_curso():
    codigo = curso_codigo.get()
    
    if codigo == '':
        messagebox.showerror('Atualizar', 'Informe o código do curso para excluir')
        return

    try:
        cursor.execute(
            'DELETE FROM cursos '
            '   WHERE id_curso=%s' ,
            (codigo,)
        )
        connection.commit()
        messagebox.showinfo('Excluir', 'Curso excluído com sucesso!')
        aluno_codigo.delete(0, END)
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao excluir curso: {e}')

# > Interface

tk = Tk()
tk.geometry('500x450')
tk.title('Revisão G2 - Sistema escolar')

# ! Frame aluno

frame_aluno = Frame(tk)
frame_aluno.grid(row=0, column=1, sticky='nw', padx=50)

Label(frame_aluno, text='Aluno', font='Bold 16').grid(row=0, column=0)

Label(frame_aluno, text='Código').grid(row=1, column=0)
aluno_codigo = Entry(frame_aluno)
aluno_codigo.grid(row=2, column=0)

Label(frame_aluno, text='Nome').grid(row=3, column=0)
aluno_nome = Entry(frame_aluno)
aluno_nome.grid(row=4, column=0)

Label(frame_aluno, text='Email').grid(row=5, column=0)
aluno_email = Entry(frame_aluno)
aluno_email.grid(row=6, column=0)

Label(frame_aluno, text='Telefone').grid(row=7, column=0)
aluno_telefone = Entry(frame_aluno)
aluno_telefone.grid(row=8, column=0)

Label(frame_aluno, text='Data de nascimento').grid(row=9, column=0)
aluno_dt_nascimento = Entry(frame_aluno)
aluno_dt_nascimento.grid(row=10, column=0)

Label(frame_aluno, text='Idade').grid(row=11, column=0)
aluno_idade = Entry(frame_aluno)
aluno_idade.grid(row=12, column=0)

Label(frame_aluno, text='Situação (Aprovado/Reprovado/Cursando)').grid(row=13, column=0)
aluno_status = Entry(frame_aluno)
aluno_status.grid(row=14, column=0)

Button(frame_aluno, text='Cadastrar', command=cadastrar_aluno).grid(row=15, column=0)
Button(frame_aluno, text='Visualizar', command=visualizar_aluno).grid(row=16, column=0)
Button(frame_aluno, text='Excluir', command=excluir_aluno).grid(row=17, column=0)
Button(frame_aluno, text='Trocar situação', command=trocar_status_aluno).grid(row=18, column=0)
Button(frame_aluno, text='Maiores de 18 anos', command=maiores_18_anos).grid(row=19, column=0)

# ! Frame curso

frame_curso = Frame(tk)
frame_curso.grid(row=0, column=2, sticky='ne', padx=50)

Label(frame_curso, text='Curso', font='Bold 16').grid(row=0, column=0)

Label(frame_curso, text='Código').grid(row=1,column=0)
curso_codigo = Entry(frame_curso)
curso_codigo.grid(row=2, column=0)

Label(frame_curso, text='Nome').grid(row=3,column=0)
curso_nome = Entry(frame_curso)
curso_nome.grid(row=4, column=0)

Label(frame_curso, text='Descrição').grid(row=5, column=0)
curso_desc = Entry(frame_curso)
curso_desc.grid(row=6, column=0)

Button(frame_curso, text='Cadastrar', command=cadastrar_curso).grid(row=7, column=0)
Button(frame_curso, text='Visualizar', command=visualizar_curso).grid(row=8, column=0)
Button(frame_curso, text='Excluir', command=excluir_curso).grid(row=9, column=0)

tk.mainloop()
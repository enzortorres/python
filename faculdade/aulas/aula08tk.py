from mysql import connector

from tkinter import *
from tkinter import messagebox 

connection = connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='',
)

cursor = connection.cursor()

# Criando a database
cursor.execute(
    'CREATE DATABASE IF NOT EXISTS loja '
)

# Usando a database
cursor.execute(
    'USE loja'
)

# Criando as tabelas
cursor.execute(
    'CREATE TABLE IF NOT EXISTS produto ('
    '   codigo INT PRIMARY KEY, '
    '   nome VARCHAR(20) NOT NULL, '
    '   preco DECIMAL(10,2) NOT NULL, '
    '   qtd INT NOT NULL '
    ') '
)

tk = Tk()
tk.geometry('500x300')
tk.title('loja')

def inserir():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    qtd = e_qtd.get()
    
    if not codigo or not nome or not preco or not qtd:
        messagebox.showerror('Inserir', 'Todos os campos são obrigatórios')
    else:
        cursor.execute(
            'INSERT INTO produto(codigo, nome, preco, qtd) VALUES'
            '(%s, %s, %s, %s)', 
            (codigo, nome, preco, qtd)
        )
        connection.commit()
        messagebox.showinfo('Sucesso', f'Produto "{nome}" inserido com sucesso.')

Label(tk,text='Código:').grid(row=0,column=0,padx=5,pady=5)
e_codigo = Entry(tk)
e_codigo.grid(row=0,column=1,padx=5,pady=5)

Label(tk,text='Nome:').grid(row=1,column=0,padx=5,pady=5)
e_nome = Entry(tk)
e_nome.grid(row=1,column=1,padx=5,pady=5)

Label(tk,text='Preço:').grid(row=2,column=0,padx=5,pady=5)
e_preco = Entry(tk)
e_preco.grid(row=2,column=1,padx=5,pady=5)

Label(tk,text='Quantidade:').grid(row=3,column=0,padx=5,pady=5)
e_qtd = Entry(tk)
e_qtd.grid(row=3,column=1,padx=5,pady=5)

frame_botoes = Frame(tk)
frame_botoes.grid(row=4, column=0, columnspan=2, pady=10)

Button(frame_botoes, text='Consultar').pack(side=LEFT, padx=5)
Button(frame_botoes, text='Inserir', command=inserir).pack(side=LEFT, padx=5)
Button(frame_botoes, text='Alterar').pack(side=LEFT, padx=5)
Button(frame_botoes, text='Excluir').pack(side=LEFT, padx=5)

tk.mainloop()
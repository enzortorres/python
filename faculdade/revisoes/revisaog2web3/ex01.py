from mysql import connector

from tkinter import *
from tkinter import messagebox

connection = connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database=''
)

cursor = connection.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS loja')

cursor.execute('use loja')

cursor.execute('''CREATE TABLE produto(
            codigo INT PRIMARY KEY,
            nome VARCHAR(20) NOT NULL,
            preco DECIMAL(10,2) NOT NULL,
            quantidade INT NOT NULL)
''')

root = Tk()
root.geometry('500x300')
root.title('Loja')

def inserir():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade = e_quantidade.get()

    if(codigo=='' or nome=='' or preco =='' or quantidade==''):
        messagebox.showerror('Inserir','Todos os campos são obrigatórios')
    else:
        cursor.execute('INSERT INTO PRODUTO (codigo,nome,preco,quantidade) VALUES (%s,%s,%s,%s)',(codigo,nome,preco,quantidade))
        connection.commit()
        messagebox.showinfo('Inserir','Produto inserido com sucesso!')

        e_codigo.delete(0, END)
        e_nome.delete(0, END)
        e_preco.delete(0, END)
        e_quantidade.delete(0, END)

def excluir():
    codigo = e_codigo.get()
    if codigo =='':
        messagebox.showerror('Excluir','Informe o codigo do produto')
    else:
        cursor.execute('DELETE FROM produto WHERE codigo = %s',(codigo,))
        connection.commit()
        messagebox.showinfo('Excluir', 'Produto excluido com sucesso!')
        e_codigo.delete(0,END)

def atualizar():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade = e_quantidade.get()

    if (codigo == '' or nome == '' or preco == '' or quantidade == ''):
        messagebox.showerror('Atualizar', 'Todos os campos saõ obrigatórios')
    else:
        cursor.execute('UPDATE produto SET nome=%s,preco=%s,quantidade=%s WHERE codigo=%s',(nome,preco,quantidade,codigo))
        connection.commit()
        messagebox.showinfo('Atualizar', 'Produto atualizado com sucesso!')

        e_codigo.delete(0, END)
        e_nome.delete(0, END)
        e_preco.delete(0, END)
        e_quantidade.delete(0, END)

def consultar():
    codigo = e_codigo.get()

    if codigo == '':
        messagebox.showerror('Selecionar', 'Informe o codigo do produto')
    else:
        cursor.execute('SELECT * FROM produto WHERE codigo=%s',(codigo,))
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                e_nome.delete(0, END)
                e_preco.delete(0, END)
                e_quantidade.delete(0, END)

                e_nome.insert(0, row[1])
                e_preco.insert(0,row[2])
                e_quantidade.insert(0, row[3])
                messagebox.showinfo('Selecionar','Selecionado com sucesso!'f'Codigo:{row[0]}\nNome:{row[1]}\nPreço{row[2]}\nQtd:{row[3]}')
        else:
            messagebox.showerror('Selecionar','produto não encontrado!')

Label(root,text='Código').place(x=20,y=30)
Label(root,text='Nome').place(x=20,y=60)
Label(root,text='Preço').place(x=20,y=90)
Label(root,text='Quantidade').place(x=20,y=120)

e_codigo = Entry(root)
e_codigo.place(x=100,y=30)

e_nome = Entry(root)
e_nome.place(x=100,y=60)

e_preco = Entry(root)
e_preco.place(x=100,y=90)

e_quantidade = Entry(root)
e_quantidade.place(x=100,y=120)

Button(root,text='Inserir',command=inserir).place(x=30,y=160)
Button(root,text='Excluir',command=excluir).place(x=80,y=160)
Button(root,text='Alterar',command=atualizar).place(x=130,y=160)
Button(root,text='Consultar',command=consultar).place(x=180,y=160)

root.mainloop()
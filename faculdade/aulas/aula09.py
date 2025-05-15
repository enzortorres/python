# from tkinter import *

# tk = Tk()
# tk.geometry('500x500')
# tk.title("Aula 09")

# men = Menu()

# arquivo_menu = Menu(tearoff=0)
# arquivo_menu.add_command(label="Novo")
# arquivo_menu.add_command(label="Salvar")
# arquivo_menu.add_command(label="Salvar como")
# arquivo_menu.add_command(label="Imprimir")
# arquivo_menu.add_command(label="Sair")
# men.add_cascade(label='Arquivo', menu=arquivo_menu)
# tk.config(menu=men)

# editar_menu = Menu(men, tearoff=0)
# editar_menu.add_command(label="Copiar")
# editar_menu.add_command(label="Colar")
# editar_menu.add_command(label="Voltar")
# editar_menu.add_command(label="Sair")
# men.add_cascade(label="Editar", menu=editar_menu)
# tk.config(menu=men)

# tk.mainloop()

# ! Para abrir nova janela

# from tkinter import *

# tk = Tk()
# tk.geometry('500x500')
# tk.title("Janela principal")

# def abrir_janela():
#     nova_janela = Toplevel(tk)
#     nova_janela.geometry('500x500')
#     nova_janela.title("Janela secundária")
#     text = Label(nova_janela, text="Esta é uma nova janela").pack()

# btn = Button(tk, text='Abrir nova', command=abrir_janela).pack()

# tk.mainloop()

# ! Para abrir nova janela pelo menu

# from tkinter import *

# tk = Tk()
# tk.geometry('500x500')
# tk.title('Janela principal')

# menu_bar = Menu(tk, tearoff=0)
# tk.config(menu=menu_bar)

# def abrir_arquivo():
#     nova_janela = Toplevel(tk)
#     nova_janela.geometry('500x500')
#     nova_janela.title('Nova janela')
#     lab = Label(nova_janela, text="Esta é uma nova janela.")
#     lab.pack()

# novo_menu = Menu(tk, tearoff=0)
# novo_menu.add_command(label="Abrir nova janela", command=abrir_arquivo)
# menu_bar.add_cascade(label="Arquivo", menu=novo_menu)

# tk.mainloop()

# ! Exemplo para abrir nova janela no objeto radiobutton

from tkinter import *

tk = Tk()
tk.geometry('500x500')
tk.title("Aula 09")

frame_para_radio = Frame(tk).pack()

s = IntVar()

def abrir_arquivo():
    nova_janela = Toplevel(tk)
    nova_janela.geometry('500x500')
    nova_janela.title("Nova janela")
    l = Label(nova_janela, text='Esta é uma nova janela')
    l.pack()

r1 = Radiobutton(tk, text="Abrir nova janela", variable=s, value=1, command=abrir_arquivo).pack()
r1 = Radiobutton(tk, text="Abrir arquivo", variable=s, value=2).pack()
r1 = Radiobutton(tk, text="Fechar arquivo", variable=s, value=3).pack()

tk.mainloop()
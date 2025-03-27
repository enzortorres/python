from tkinter import *

bg_black = '#303030'

tk = Tk()
tk.title('Hello world!')
tk.geometry('600x300')

# tk['bg'] = 'grey' # > Pode definir a cor com hexadecimal e com nomemclatura
# tk.resizable(width=False, height=False) # > Para impossibilitar o redimensionamente da janela
# tk.wm_iconbitmap('./favicon.ico') # > Para colocar um icone na janela
# tk.state('zoom') # > Para iniciar a janela em tela cheia
# tk.state('iconic') # > Para iniciar com a janela minimizada
# tk.maxsize(width='900', height='500') # > Para definir o tamanho máximo que a janela pode chegar
# tk.minsize(width='300', height='200') # > Para definir o tamanho mínimo que a janela pode chegar

# ! Entry() - criar uma caixa de entrada(input) na janela

# e = Entry(tk)
# e.pack(pady=20)

# # ! Button() - inserir um botão na janela

# btn = Button(tk, text='Inserir', font='Verdana 12 bold').pack()

# def botao_clicado():
#     label.config(text='Oi, você clicou no botão')

# btn1 = Button(tk, text='Clique aqui', font='Verdana 12 bold', fg='white', bg='#4CAF50', # > fg = cor da fonte
#             relief='raised', # > Para inserir uma borda
#             bd=5, padx=20, pady=10, # > bd=5 para definir a largura da borda, pad = padding
#             activebackground='#45a049', # > Alterar a cor do fundo ao clicar no botão
#             activeforeground='yellow', # > Alterar a cor da fonte ao clicar
#             command=botao_clicado
# )
# btn1.pack(pady=20)

# label = Label(tk,
#             bg='#CECECE',
#             fg='white',
#             width=30,
#             height=1
# )
# label.pack()

# # ! grid - trabalha com linha e coluna

# x1 = Label(tk, text='Teste 1', bg='red')
# x2 = Label(tk, text='Teste 2', bg='yellow')
# x3 = Label(tk, text='Teste 3', bg='orange')

# x1.grid(row=0, column=0, padx=10)
# x2.grid(row=1, column=1, padx=10)
# x3.grid(row=2, column=2, padx=10)

# # ! Input com nome e idade

# label_nome = Label(tk, text='Nome', font='Arial, 10')
# label_nome.grid(row=0, column=0,padx=10,pady=10)
# entry_nome = Entry(tk)
# entry_nome.grid(row=0, column=1,padx=10,pady=10)

# label_idade = Label(tk, text='Idade:', font='Arial, 10')
# label_idade.grid(row=1, column=0, padx=10, pady=10)
# entry_idade = Entry(tk)
# entry_idade.grid(row=1, column=1, padx=10, pady=10)

# def informacoes():
#     nome = entry_nome.get()
#     idade = entry_idade.get()
#     r_label.config(text = f'Nome: {nome}\nIdade: {idade}')

# btn2 = Button(tk, text='Cadastrar', command=informacoes)
# btn2.grid(row=2, column=0, columnspan=2, padx=20)
# r_label = Label(tk, bg='#CECECE', width=30, height=2)
# r_label.grid(row=3, column=0, columnspan=2)

# # ! Checkbutton() - para seleção múltipla
# futebol_var = IntVar()
# basquete_var = IntVar()
# natacao_var = IntVar()
# ciclismo_var = IntVar()
# tenis_var = IntVar()
# volei_var = IntVar()
# surf_var = IntVar()

# t = Label(tk, text='Qual o seu esporte favorito')
# a1 = Checkbutton(tk, text='Futebol', variable=futebol_var)
# a2 = Checkbutton(tk, text='Basquete', variable=basquete_var)
# a3 = Checkbutton(tk, text='Natação', variable=natacao_var)
# a4 = Checkbutton(tk, text='Ciclismo', variable=ciclismo_var)
# a5 = Checkbutton(tk, text='Tênis', variable=tenis_var)
# a6 = Checkbutton(tk, text='Vôlei', variable=volei_var)
# a7 = Checkbutton(tk, text='Surf', variable=surf_var)

# # t.grid(row=0, column=0, padx=10)
# # a1.grid(row=1, column=0, padx=10)
# # a2.grid(row=2, column=0, padx=10)
# # a3.grid(row=3, column=0, padx=10)
# # a4.grid(row=4, column=0, padx=10)
# # a5.grid(row=5, column=0, padx=10)
# # a6.grid(row=6, column=0, padx=10)
# # a7.grid(row=7, column=0, padx=10)

# t.place(x=10, y=10)
# a1.place(x=10, y=30)
# a2.place(x=80, y=30)
# a3.place(x=155, y=30)
# a4.place(x=223, y=30)
# a5.place(x=295, y=30)
# a6.place(x=348, y=30)
# a7.place(x=406, y=30)

# checkboxs = [a1, a2, a3, a4, a5, a6, a7]

# def mostrar_selecionados():
#     selecionados = []
#     if futebol_var.get():
#         selecionados.append('Futebol')
#     if basquete_var.get():
#         selecionados.append('Basquete')
#     if natacao_var.get():
#         selecionados.append('Natação')
#     if ciclismo_var.get():
#         selecionados.append('Ciclismo')
#     if tenis_var.get():
#         selecionados.append('Tênis')
#     if volei_var.get():
#         selecionados.append('Vôlei')
#     if surf_var.get():
#         selecionados.append('Surf')
#     r_label.config(text=f'Esporte(s) selecionado(s): '+' | '.join(selecionados))

# btn4 = Button(tk, text='Mostrar selecionados', command=mostrar_selecionados) 
# btn4.place(x=10, y=60)

# r_label = Label(tk, text='Esportes selecionados: Nenhum')
# r_label.place(x=10, y=90)

# ! Radiobutton() - Para seleção simples

# valor = IntVar()

# r1 = Radiobutton(tk, text='Opcão 1', variable=valor, value=1)
# r2 = Radiobutton(tk, text='Opcão 2', variable=valor, value=2)
# r3 = Radiobutton(tk, text='Opcão 3', variable=valor, value=3)

# r1.place(x=10, y=10)
# r2.place(x=90, y=10)
# r3.place(x=170, y=10)

# ! Listbox() - cria uma lista 

lista = Listbox(tk, selectmode=MULTIPLE)
lista.insert(END, 'AC')
lista.insert(END, 'AM')
lista.insert(END, 'AL')
lista.insert(END, 'MG')
lista.insert(END, 'RJ')
lista.insert(END, 'SP')
lista.insert(END, 'TO')
lista.pack()

estados = ['a', 'b', 'c']
for estado in estados:
    lista.insert(END, estado)

tk.mainloop() # > Para rodar o app
from tkinter import *

def is_bissexto():
    ano = int(ano_entry.get())
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        res_label.config(text="É bissexto.")
    else:
        res_label.config(text="Não é bissexto.")

tk = Tk()
tk.geometry('500x300')
tk.title('REVISAO 1 EX03')

ano_text = Label(tk, text="Digite o ano que deseja checar se é bissexto")
ano_text.grid(row=0, column=0)
ano_entry = Entry(tk)
ano_entry.grid(row=1, column=0)

btn = Button(tk, text="Clique aqui", command=is_bissexto)
btn.grid(row=2, column=0)

res_label = Label(tk, text="")
res_label.grid(row=3, column=0)

tk.mainloop()
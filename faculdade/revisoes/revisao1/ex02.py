from tkinter import *

def out_of_limit():
    lista = entry.get().strip().split(",")
    limite = int(limite_entry.get())
    
    in_limit = True
    for num in lista:
        if int(num) > limite:
            label_res.config(text=f"O número no índice {lista.index(num)} passou do limite.")
            in_limit = False
            break
    
    if in_limit:
        label_res.config(text=-1)

tk = Tk()
tk.geometry('500x300')
tk.title('REVISAO1 EX02')

entry_text = Label(tk, text="Digite uma lista separada por ','")
entry_text.grid(row=0, column=0)
entry = Entry(tk)
entry.grid(row=1,column=0)

limite_text = Label(tk, text="Digite o limite da lista")
limite_text.grid(row=2, column=0)
limite_entry = Entry(tk)
limite_entry.grid(row=3,column=0)

btn = Button(tk, text="Clique aqui", command=out_of_limit)
btn.grid(row=4, column=0)

label_res = Label(tk)
label_res.grid(row=5, column=0)

tk.mainloop()
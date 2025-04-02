from tkinter import *

def verificar_numero(num):
    num = num.get()
    if int(num) >= 0:
        res = 'Positivo'
    else:
        res = 'Negativo'
    res_label.config(text=res)
tk = Tk()
tk.geometry('500x300')
tk.title('REVISAO 1 EX01')

entry = Entry(tk)
entry.grid(row=0, column=0)

btn = Button(tk, text='Clique aqui', command=lambda: verificar_numero(entry))
btn.grid(row=2, column=0)

res_label = Label(tk, text='')
res_label.grid(row=1, column=0)

tk.mainloop()
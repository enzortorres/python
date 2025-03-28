from tkinter import *

tk = Tk()
tk.title('TDE5 EX01')
tk.geometry('600x400')

texto_entry = Label(tk, text="Digite um número: ", relief="flat", width=20,height=2)
texto_entry.grid(row=0,column=0, padx=5 ,pady=5)

entry = Entry(tk)
entry.grid(row=1, column=0, padx=5, pady=5)

texto_resultado = Label(tk, text='Aqui vai sair o resultado', width=20, height=2)
texto_resultado.grid(row=2, column=0, padx=5, pady=5)

def positivo_ou_negativo():
    if int(entry.get()) > 0:
        texto_resultado.config(text="Positivo")
    else:
        texto_resultado.config(text="Negativo")

button = Button(tk, text='Clique aqui', command=positivo_ou_negativo)
button.grid(row=3, column=0)
tk.mainloop()
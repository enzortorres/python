from tkinter import *

def buscar_limite():
    lista = entry.get().split(',')
    limite = limite_entry.get()
    index = -1
    
    for number in lista:
        if int(number) > int(limite):
            index = lista.index(number)
            break
    resultado.config(text=f"{index}")
        
tk = Tk()
tk.title('TDE 5 EX2')
tk.geometry('500x300')

texto_entry = Label(tk, text="Digite uma lista de números: ", pady=5)
texto_entry.grid(row=0, column=0)

entry = Entry(tk)
entry.grid(row=1, column=0)

limite_texto_entry = Label(tk, text="Digite o valor limite da lista:", pady=5)
limite_texto_entry.grid(row=2, column=0)

limite_entry = Entry(tk)
limite_entry.grid(row=3, column=0)

button = Button(tk, text="Clique aqui", command=buscar_limite)
button.grid(row=4, column=0)

resultado = Label(tk, text="Aqui vai sair o resultado", pady=5)
resultado.grid(row=5, column=0)

tk.mainloop()
from tkinter import *

def ano_bissexto():
    ano = int(entry_ano.get()) 
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        resultado.config(text="O ano é bissexto!")
        return
    resultado.config(text="O ano não é bissexto!")

tk = Tk()
tk.title('TDE 05 EX03')
tk.geometry('500x300')

frame = Frame(tk, bg='#CECECE', padx=10, pady=10)
frame.grid(row=0, column=0)

texto_entry = Label(frame, text="Digite o ano atual:", padx=10, pady=10)
texto_entry.grid(row=0, column=0)

entry_ano = Entry(frame)
entry_ano.grid(row=1, column=0)

btn = Button(frame, text="Clique aqui", command=ano_bissexto)
btn.grid(row=2, column=0)

resultado = Label(frame, text="O resultado vai sair aqui!", pady=10)
resultado.grid(row=3, column=0)

tk.mainloop()
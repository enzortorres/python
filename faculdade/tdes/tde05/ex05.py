from tkinter import *

def info_lista():
    lista = entry_numbers.get().split(",")
    lista = [int(n) for n in lista]
    pares = [
        n for n in lista
        if n % 2 == 0
    ]
    
    if 3 in lista:
        index_3 = lista.index(3)
    else:
        index_3 = -1
    
    resultado.config(text=f"""\
O número 9 apareceu {lista.count(9)} vezes.
O número 3 apareceu a primeira vez no índice {index_3}.
Os números pares são: {pares}""", justify="left"
)

tk = Tk()
tk.title('TDE05 EX05')
tk.geometry('300x200')

frame = Frame(tk, bg="#CECECE", width=300, height=200)
frame.place(x=0, y=0)

label = Label(frame, text='Digite uma lista de números, separados por ",".')
label.place(x=5, y=5)

entry_numbers = Entry(frame)
entry_numbers.place(x=5, y=30)

btn = Button(frame, text="Clique aqui", command=info_lista)
btn.place(x=5, y=55)

resultado = Label(frame, text="O resultado sairá aqui", anchor='w')
resultado.place(x=5, y=85)

tk.mainloop()
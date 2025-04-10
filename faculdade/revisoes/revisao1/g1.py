def fahrenheit():
    try:
        c = float(entry_celsius.get())
        res = (c*9/5) + 32
        label_res.config(text=f"{res}F")
    except:
        label_res.config(text="ERRO! Somente números!")
        
def kelvin():
    try:
        c = float(entry_celsius.get())
        res = c + 275.15
        label_res.config(text=f"{res}K")
    except:
        label_res.config(text="ERRO! Somente números!")

from tkinter import *

tk = Tk()
tk.title("Conversor de Temperaturas")
tk.geometry('500x300')

label = Label(tk, text="Digite uma temperatura em Celsius")
label.grid(row=0, column=0)

entry_celsius = Entry(tk)
entry_celsius.grid(row=1, column=0)

btn_fahrenheit = Button(tk, text="Converta para Fahrenheit", command=fahrenheit)
btn_fahrenheit.grid(row=2, column=0)

btn_kelvin = Button(tk, text="Converta para Kelvin", command=kelvin)
btn_kelvin.grid(row=2, column=1)

label_res = Label(tk, text="Aqui sai o resultado")
label_res.grid(row=3, column=0)

tk.mainloop()
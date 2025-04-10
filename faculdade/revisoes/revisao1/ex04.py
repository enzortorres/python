from tkinter import *

def calculadora():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res_label.config(
        text=f"Adição: {num1} + {num2} = {num1+num2}\n" +
            f"Subtração: {num1} - {num2} = {num1-num2}\n" + 
            f"Multiplicação: {num1} x {num2} = {num1*num2}\n" +
            (f"Divisão: {num1} ÷ {num2} = {num1/num2}" if num2 != 0 else "Não pode dividir nada por 0.")
    )

tk = Tk()
tk.geometry('500x300')
tk.title('REVISAO1 EX04')

number1_label = Label(text="Digita o primeiro número")
number1_label.grid(row=0, column=0)
number1_entry = Entry(tk)
number1_entry.grid(row=1, column=0)

number2_label = Label(text="Digita o segundo número")
number2_label.grid(row=2, column=0)
number2_entry = Entry(tk)
number2_entry.grid(row=3, column=0)

btn = Button(tk, text="Clique aqui", command=calculadora)
btn.grid(row=4, column=0)

res_label = Label(tk, text="", justify="left")
res_label.grid(row=5, column=0)

tk.mainloop()
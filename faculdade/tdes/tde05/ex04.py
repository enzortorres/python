from tkinter import *

def soma():
    number1 = int(entry_number1.get())
    number2 = int(entry_number2.get())
    resultado.config(text=number1+number2)
    
def subtracao():
    number1 = int(entry_number1.get())
    number2 = int(entry_number2.get())
    resultado.config(text=number1-number2)
    
def multiplicacao():
    number1 = int(entry_number1.get())
    number2 = int(entry_number2.get())
    resultado.config(text=number1*number2)
    
def divisao():
    number1 = int(entry_number1.get())
    number2 = int(entry_number2.get())
    
    if number1 == 0 or number2 == 0:
        resultado.config(text="Não pode dividir com 0")
        return
    resultado.config(text=number1/number2)

tk = Tk()
tk.title('TDE05 EX 04')
tk.geometry('350x200')
tk.resizable(0,0)

frame = Frame(tk, bg="#CECECE", width=500, height=300)
frame.place(x=0, y=0)
frame.grid_propagate(False)

label = Label(frame, text="Digite dois números e depois selecione a operação que deseja")
label.place(x=10,y=5)

# > Inputs dos números

entry_number1 = Entry(frame)
entry_number1.place(x=10, y=30)

entry_number2 = Entry(frame)
entry_number2.place(x=150, y=30)

# > Botões das operações

oper_soma = Button(frame, text="+", command=soma)
oper_soma.place(x=10, y=60)

oper_subtracao = Button(frame, text="-", command=subtracao)
oper_subtracao.place(x=30, y=60)

oper_multiplicacao = Button(frame, text="*", command=multiplicacao)
oper_multiplicacao.place(x=50, y=60)

oper_divisao = Button(frame, text="/", command=divisao)
oper_divisao.place(x=70, y=60)

# > Resultado

resultado = Label(frame, text="Aqui vai sair o resultado")
resultado.place(x=10, y=100)

tk.mainloop()
from tkinter import *

tk = Tk()
tk.title("Button Test")
tk.geometry("1920x1080")

label = Label(tk, text='First button in tkinter', font=("JetBrains Mono", 14))
label.grid(column=0, row=0)

def ola():
    print('Olá Mundo!, Eu sou o mudinho!')
    label.configure(text='Olá Mundo!, Eu sou o mudinho!')

button = Button(tk, text="Click Here", command=ola)
button.grid(column=2, row=0)

tk.mainloop()
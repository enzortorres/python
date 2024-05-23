import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox


root = tk.Tk()
root.title('Eai')
root.geometry("1920x1080")
root.configure(background='#ffffff')


def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        'VAMO', 'Já tira a calcinha rs')


def denied():
    button_1.destroy()


margin = Canvas(root, width=500, bg='#ffffff', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#ffffff', text='Vamo fude hoje?',
                fg='#0f0f0f', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#ffffff', command=denied,
                    relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text='Sim', bg='#ffffff', relief=RIDGE,
                    bd=3, command=accepted, font=('Montserrat', 14, 'bold'), width=10, height=3)
button_2.pack()


root.mainloop()

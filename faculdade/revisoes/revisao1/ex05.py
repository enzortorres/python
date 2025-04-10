from tkinter import *

def infos_lista():
    qtd_nove = 0
    pares = []
    index_tres = 0
    try:
        numeros = entry.get().strip().split(",")
        numeros = [int(num) for num in numeros]
        
        qtd_nove = numeros.count(9)
        pares = [num for num in numeros if num % 2 == 0]
        index_tres = numeros.index(3)
        
    except:
        index_tres = -1
    finally:
        res_label.config(
            text=f"O número 9 apareceu {qtd_nove} vezes\n" \
                f"A primeira ocorrência do número 3 foi no índice {index_tres}\n" \
                f"Os números pares digitados foram: {pares}"
        )        

tk = Tk()
tk.geometry('500x300')
tk.title('REVISAO1 EX05')

text_label = Label(tk, text="Digite uma lista de 4 números separados por ','")
text_label.grid(row=0, column=0)

entry = Entry(tk)
entry.grid(row=1, column=0)

btn = Button(tk, text="Clique aqui", command=infos_lista)
btn.grid(row=2, column=0)

res_label = Label(tk, text="", justify="left")
res_label.grid(row=3, column=0)


tk.mainloop()
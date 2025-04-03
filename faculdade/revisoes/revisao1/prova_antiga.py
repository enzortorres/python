"""
    ? Questão 1 (0,5 ponto): Qual comando é usado para iniciar a interface gráfica de um aplicativo Tkinter?
    a) tkinter.show()
    * b) tkinter.mainloop() 
    c) tkinter.run()
    d) tkinter.start()
    > b)

    ? Questão 2 (1,0 ponto): O que acontece quando ocorre uma exceção em Python, mas não é capturada por um bloco try-except?
    a) O programa continua normalmente
    b) O programa entra em um loop infinito
    * c) O programa exibe um erro e para a execução
    d) O programa corrige o erro automaticamente

    ? Questão 3 (1,0 ponto): Considere o código abaixo:
    : count = 0
    : while count < 5:
    :     count += 1
    :     if count == 3:
    :         continue
    :     print(count)
    : else:
    :     print("Laço concluído.")

    ? Qual será a saída desse programa?
    * a) 1 2 4 5 Laço concluído.
    b) 1 2 3 4 5 Laço concluído.
    c) 1 2 4 5
    d) 1 2 3 4 5

    ? Questão 4 (0,5 ponto): Qual será a saída do seguinte código?
    : numeros = [1, 2, 3, 4, 5]
    : resultado = [x**2 for x in numeros if x % 2 == 0]
    : print(resultado)

    * a) [4, 16]
    b) [1, 9, 25]
    c) [4, 9, 16]
    d) [4, 8]

    ? Questão 5 (1,0 ponto): Analise o script Python exibido a seguir.
    : x = 1
    : y = 1
    : while x < 100:
    :   x, y = y, x + y
    :   if x % 3 == 0:
    :       print(x)

    ? O código acima utiliza um loop while para calcular e imprimir os primeiros números da sequência de Fibonacci que são múltiplos de 3. Qual é a sequência correta de valores impressos pelo código?
    
    * a) 3, 21, 144
    b) 3, 5, 21, 55
    c) 3, 8, 21, 55
    d) 3, 13, 55, 233
    e) Nenhuma das alternativas
    
    ? Questão 6 (1,0 ponto): O que o método pack() faz em Tkinter?
    * a) Adiciona um widget ao layout da janela, organizando-o automaticamente.
    b) Cria um botão.
    c) Define a cor de fundo de um widget.
    d) Exibe uma caixa de diálogo de erro.
    
    ? Questão 7 (1,0 ponto): Em Tkinter, qual o efeito de usar o método grid() ao invés de pack() para organizar widgets?
    * a) grid() organiza widgets em colunas e linhas, enquanto pack() organiza em relação aos lados da janela.
    b) grid() sobrepõe widgets, enquanto pack() os empilha verticalmente.
    c) grid() organiza widgets em uma grade fixa, enquanto pack() usa tamanhos dinâmicos.
    d) grid() só pode ser usado com o widget Frame, enquanto pack() pode ser usado com qualquer widget.

    ? Questão 8 (1,0 ponto): Considere o seguinte código:
    : import tkinter as tk
    : def verificar():
    :   if var.get() == 1:
    :       print("Selecionado")
    :   else:
    :       print("Desmarcado")
    
    : janela = tk.Tk()
    : var = tk.IntVar()
    : checkbox = tk.Checkbutton(janela, text="Aceito", variable=var, command=verificar)
    : checkbox.pack()
    : janela.mainloop()

    ? O que será impresso ao clicar repetidamente na caixa de seleção?
    * a) "Selecionado" será impresso sempre que o botão for clicado.
    b) "Desmarcado" será impresso sempre que o botão for clicado.
    c) Alternará entre "Selecionado" e "Desmarcado".
    d) Nada será impresso.
    
    ? Questão 9 (1,0 ponto): Como você adiciona um elemento à lista minha_lista?
    a) minha_lista.add("novo_elemento")
    * b) minha_lista.append("novo_elemento")
    c) minha_lista.insert("novo_elemento")
    d) minha_lista.update("novo_elemento")
    
    ? Questão 10 (2,0 pontos): Desenvolver uma aplicação em Python utilizando Tkinter para criar uma interface gráfica que receba um dicionário, onde as chaves são nomes de produtos e os valores são os preços correspondentes. A função deve:
    : ● Solicitar que o usuário insira o nome de um produto.
    : ● Se o produto estiver no dicionário, exibir o preço.
    : ● Se não estiver, permitir que o usuário insira o preço e adicionar o novo produto ao dicionário.
    : ● O programa deve continuar até que o usuário digite "sair".
"""

from tkinter import *


def verificar_produto():
    nome_produto = entry_produto.get().strip()
    
    for produto in produtos:
        if nome_produto in produto.values():
            res_label.config(text=f"Preço: R${produto['preco']}")
            break
        if not hasattr(verificar_produto, "preco_entry"):
            res_label.config(text="Produto não encontrado!\nDigite um preço para seu produto: ")
            
            preco_entry = Entry(tk)
            preco_entry.grid(row=4, column=0)
            
            btn_cadastrar = Button(tk, text="Cadastrar produto", command=lambda: cadastrar_produto())
            btn_cadastrar.grid(row=5, column=0)
        if nome_produto == "sair":
            tk.destroy()
    def cadastrar_produto():
        nome_produto = entry_produto.get().strip()
        preco_produto = int(preco_entry.get())
    
        produtos.append({'nome': nome_produto, 'preco': preco_produto})
        res_label.config(text=f"{nome_produto} cadastrado com sucesso!")
        preco_entry.destroy()
        btn_cadastrar.destroy()

produtos = [
    {}
]

tk = Tk()
tk.geometry('500x300')
tk.title('QUESTÃO 10 REVISÃO')

text_label = Label(tk, text="Digite o nome de um produto")
text_label.grid(row=0, column=0)

entry_produto = Entry(tk)
entry_produto.grid(row=1, column=0)

btn_verificar = Button(tk, text="Clique aqui", command=verificar_produto)
btn_verificar.grid(row=2, column=0)

res_label = Label(tk, text="")
res_label.grid(row=3, column=0)

tk.mainloop()
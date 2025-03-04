"""
    | split e join com list e str
    * split - divide uma string, cortando onde tem espaços, \n, \t, \r, \f.
    * strip - remove os espaços da esquerda e da direita, existe também o lstrip e o rstrip para lados específicos.
    * join - une tudo em uma string.
"""

frase = 'region them touch weigh read manufacturing metal electricity ranch knew mysterious'

lista_palavras = frase.split()
print(lista_palavras)

print("\n" + "=" * 50 + "\n")

frases_unidas = ", ".join(lista_palavras)
print(frases_unidas)

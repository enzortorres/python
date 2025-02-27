frase = '''O Python é uma linguagem de programação
multiparadigma.
Python foi criado por Guido van Rossum'''

i = 0
qtd_letra_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''


while i < len(frase):
    if frase[i] != ' ' and frase[i] != letra_apareceu_mais_vezes:
        letra_atual = frase[i]
    
    qtd_letra = frase.count(letra_atual)
    
    if qtd_letra > qtd_letra_apareceu_mais_vezes:
        
        qtd_letra_apareceu_mais_vezes = qtd_letra
        letra_apareceu_mais_vezes = letra_atual
    
    print(letra_atual)
    i += 1

print(f'A letra que apareceu mais vezes foi: "{letra_apareceu_mais_vezes}", aparecendo {qtd_letra_apareceu_mais_vezes} vezes na frase.')
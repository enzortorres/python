def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)

texto = str(input('O que você deseja escrever? '))

escreva(texto)
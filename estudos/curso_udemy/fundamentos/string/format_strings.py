def linha():
    print("\n" + "=" * 20, end="\n\n")

nome = "Enzo"
preco = 1500
var = '%s, o preço é R$%.2f' % (nome, preco)
print(var)
print('O hexadecimal de %d é %08x' % (1500, 1500)) 

linha()

var = 'ABC'
print(f'{var}')
print(f'{var: >10}.')
print(f'{var: <10}.')
print(f'{var:-^25}')
print(f'{var}')
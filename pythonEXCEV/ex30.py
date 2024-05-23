num = int(input('Digite um valor: '))
resultado = num % 2
if resultado == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é impar!'.format(num))
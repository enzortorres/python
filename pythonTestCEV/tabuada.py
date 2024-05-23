from time import sleep
random = 0
mun = 1
valor = int(input('Digite um valor: '))
while random == 0:
    print('{} x {} = {}'.format(valor, mun, valor * mun))
    mun += 1
    sleep(1)


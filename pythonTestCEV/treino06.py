from time import sleep
num = int(input('Digite um valor: '))
random = 0
mul = 1
while random == 0:
    print('{} x {:2} = {}'.format(num, mul, num * mul))
    mul += 1
    sleep(0.75)



from random import randint
from time import sleep

bot = randint(0,10)

print('Tente adivinhar...')

while True:
    choice = int(input("Qual o seu palpite? "))
    if choice == bot:
        print('Acertou!✔')
        break
    else:
        print("Errou!❌")
        sleep(0.3)
from random import randint
from time import sleep
num = randint(0, 5)

print("\033[33m-=-"*10)
print("\033[36mVou pensar em um número entre 0 e 5. Tente adivinhar...")
print("\033[33m-=-\033[m"*10)

escolha = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(0.5)
if(escolha == num):
    print("PARABÉNS! Você conseguiu!")
else:
    print("Você errou!")
    print(f"O número era {num}")
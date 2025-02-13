from random import randint

choices = ('cara', 'coroa')
print(choices)

player = int(input("""Escolha sua jogada:
0 - Cara
1 - Coroa
>>> """))

bot = randint(0,1)


if player == bot:
    print(f"Você ganhou! você escolheu {choices[player - 1]} e o computador escolheu {choices[bot]}")
else: 
    print(f"Você perdeu! você escolheu {choices[player - 1]} e o computador escolheu {choices[bot]}")
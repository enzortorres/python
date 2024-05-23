resposta = 'S'
soma = total = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('\033[33mDigite um número:\033[30m '))
    soma += numero
    total += 1
    if total == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('\033[34mQuer continuar? [S/N]\033[30m ')).upper().strip()[0]
media = soma / total
print('''\033[35mVocê digitou \033[4;35m{}\033[0;35m números e sua média foi \033[4;35m{:.2f}
\033[0;35mO maior valor foi \033[4;35m{}\033[0;35m e o menor foi \033[4;35m{}\033[m'''.format(total, media, maior, menor))
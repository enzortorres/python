n1 = float(input('\033[0;33mPrimeira nota do aluno(a): \033[m'))
n2 = float(input('\033[0;33mSegunda nota do aluno(a): \033[m'))
media = (n1 + n2)/2
lista = [5, 6.9]
if media > 10 or media < 0 :
    print('\033[0;31mNOTA INVÁLIDA!')
elif media >= 7:
    print('\033[0;32mAPROVADO')
elif media >= 5 and media < 6.9:
    print('\033[0;31mRECUPERAÇÃO!')
elif media < 5:
    print('\033[0;31mREPROVADO!')

    
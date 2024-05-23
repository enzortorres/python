print('\033[0;35m=-=x'*10)
vel = int(input('\033[4;30mQual era a velocidade do carro?\033[0;32m '))
print('\033[0;35m=-=x'*10)
multa = (vel - 80) * 7
if vel <=80:
    print('\033[0;32mSem multa!')
else:
    print('\033[1;4;31mMultado!\033[0;33m O valor da multa será de \033[1;4;32mR${}\033[0;33m!!!'.format(multa))
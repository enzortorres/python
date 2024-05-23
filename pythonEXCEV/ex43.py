#IMC = Peso ÷ (Altura × Altura)
peso = float(input('\033[0;33mQual o seu peso? \033[0;30m'))
altura = float(input('\033[0;33mQual a sua altura? \033[0;30m'))
imc = peso / (altura ** 2)
print('\033[0;36mVocê possui um IMC de {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[0;32mAbaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('\033[0;32mPeso ideal.')
elif imc >= 25 and imc < 30:
    print('\033[0;32mSobrepeso.')
elif imc >= 30 and imc < 40:
    print('\033[0;32mObesidade.')
elif imc > 40:
    print('\033[0;32mObesidade mórbida.')


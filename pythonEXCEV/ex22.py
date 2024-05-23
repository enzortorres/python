nome = str(input('Digite seu nome completo:  '))
esp = nome.replace(' ', '')
separa = nome.split()
print(f'''Analisando seu nome...
Seu nome em maiúsculas é {nome.upper()}
Seu nome em minúsculas é {nome.lower()}''')
print('''Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras'''.format(len(nome.replace(' ', '')),separa[0],nome.find(' ')))


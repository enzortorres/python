a = input('\033[33mDigite algo:\033[30m ')
#print('O tipo primitivo desse valor é',type(a))
#print('Só tem espaços?',a.isspace())
#print('É um número?',a.isnumeric())
#print('É alfabetico?',a.isalpha())
#print('É alfanumérico?',a.isalnum())
##print('Está em maiúsculas?',a.isupper())
#print('Está em minúsculas?',a.islower())
#print('Está capitalizada?',a.istitle())
print(f'''\033[34mO tipo primitivo desse valor é\033[30m {type(a)}
\033[34mSó tem espaços?\033[30m {a.isspace()}
\033[34mÉ um número?\033[30m {a.isnumeric()}
\033[34mÉ alfabetico?\033[30m {a.isalpha()}
\033[34mÉ alfanumérico?\033[30m {a.isalnum()}
\033[34mEstá em maiúsculas?\033[30m {a.isupper()}
\033[34mEstá em minúsculas?\033[30m {a.islower()}
\033[34mEstá capitalizada?\033[30m {a.istitle()}\033[m''')
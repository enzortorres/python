a = input('\033[33mDigite algo: \033[35en   m')

print(f'\033[36mO tipo primitivo desse valor é \033[30m{type(a)}')
print(f'\033[36mSó tem espaços? \033[30m{a.isspace()}')
print(f'\033[36mÉ um número? \033[30m{a.isnumeric()}')
print(f'\033[36mÉ alfabético? \033[30m{a.isalpha()}')
print(f'\033[36mÉ alfanumérico? \033[30m{a.isalnum()}')
print(f'\033[36mEstá em maiúsculas? \033[30m{a.isupper()}')
print(f'\033[36mEstá em minúsculas? \033[30m{a.islower()}')
print(f'\033[36mEstá capitalizada? \033[30m{a.istitle()}\033[m')
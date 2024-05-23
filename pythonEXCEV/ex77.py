words = ('aprender', 'programar', 'linguagem'
        , 'python', 'curso', 'grátis', 'estudar')
for p in words:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáãàâeéèêëiíìïîoóòöõôuúùuüû':
            print(letra, end=' ')

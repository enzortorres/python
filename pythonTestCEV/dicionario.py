filme = {
    'titulo':'Star Wars',
    'ano':1997,
    'diretor':'George Lucas'
}
print(filme.keys())
print(filme.values())
print(filme.items())

for keys, valeus in filme.items():
    print(f'O {keys} é {valeus}')

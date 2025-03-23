import sys

# ! Generator são funções que sabem pausar, todo generator é um iterator, mas um iterator não é um generator
lista = [n for n in range(10000)]
generator = (n for n in range(10000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)
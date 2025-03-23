iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # > tem __iter__ e __next__
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))

lista = [0,1,2]
lista = iter(lista)

for i in range(3):
    print(next(lista))
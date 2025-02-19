def linha():
    print('=' * 30)

# tuple, list, dict
# tuple = (), list = [], dict = {}


#! tuple

# tuple = ('arroz', 'carro')
# print(tuple)
# print(len(tuple))



#! list


#! Method	    Description

#* append()	    Adds an element at the end of the list
#* clear()	    Removes all the elements from the list
#* copy()	    Returns a copy of the list
#* count()	    Returns the number of elements with the specified value
#* extend()	    Add the elements of a list (or any iterable), to the end of the current list
#* index()	    Returns the index of the first element with the specified value
#* insert()	    Adds an element at the specified position
#* pop()	        Removes the element at the specified position
#* remove()	    Removes the item with the specified value
#* reverse()	    Reverses the order of the list
#* sort()	    Sorts the list


list = ['comida', 'carro']
#? list = list(('comida', 'carro'))

print(list)
print(len(list))

list.append('barco')
print(list)
print(len(list))

list.pop()
print(list)
print(len(list))

list.insert(1, 'avião')
print(list)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)
print(tropical)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)
print(thislist)

for item in thislist:
    print(item)   

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])  

[print(x) for x in thislist]



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
linha()

#! OR

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [item for item in fruits if "a" in item]

print(newlist)
linha()

newlist.reverse()
print(newlist)
linha()

newlist.sort()
print(newlist)
linha()

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
linha()

def myfunc(n):
    return abs(n - 50) #* retorna o valor absoluto da distância do valor digitado, padrão sendo 0, nesse caso o valor é 50

thislist = [100, 50, 65, 82, 23]
print(thislist)
linha()

thislist.sort(key = myfunc)

print(thislist)
linha()

list = ['apple', 'orange', 'cherry']
mylist = list[:]
print(mylist)
linha()

#! dict

# dict = {
#     'comida': 'arroz',
#     'transporte':  'carro'
# }
# for item, valor in dict.items():
#     print(f'{item.capitalize()}: {valor}')


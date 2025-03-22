# isistance() - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2),
    {0,1}, {'nome': 'Enzo'},
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance((item), bool), "SET")
        
    elif isinstance(item, str):
        print(item.upper(), isinstance((item), bool), "STR")
        
    elif isinstance(item, (int, float)):
        print(item * 2, isinstance(item, (int, float)), "NUM")
    
    else:
        print(item, "OUTRO")
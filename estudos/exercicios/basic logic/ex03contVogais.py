def contVogais(String):
    vogais = ['a', 'e', 'i', 'o', 'u']
    cont = 0

    for char in String:
        if char.lower() in vogais:
            cont += 1
    
    return cont

print(contVogais("Enzo"))

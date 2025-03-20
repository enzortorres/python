letras = set()

while True:
    letra = input("Digite: ")
    if len(letra) == 1:
        letras.add(letra)
    if 'e' in letras:
        print("ACERTOU!")
        break
    else:
        print("somente letras")
    print(letras)
try: 
    name = str(input("Digite o seu nome: "))
    name_size = len(name)
    if name_size <= 0:
        print("Digite um nome válido.")
    elif name_size <= 4:
        print("Seu nome é curto.")
    elif name_size <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")
except:
    print("Digite um nome válido.")
    
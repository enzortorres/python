try:
    hora = int(input("Digite a hora atual (00 - 23): "))
    if hora < 11:
        print("Bom dia!")
    elif hora < 17:
        print("Boa tarde!")
    elif hora < 23:
        print("Boa noite!")
    else:
        print("Horário inválido!")
except:
    print("Digite um valor válido!")
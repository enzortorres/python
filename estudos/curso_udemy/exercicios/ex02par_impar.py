try:
    number = int(input("Digite um número inteiro: "))
    if number % 2 == 0:
        print("Número par.")
    else:
        print("Número ímpar.")
except:
    print("\033[31mDigite um valor válido.\033[m")
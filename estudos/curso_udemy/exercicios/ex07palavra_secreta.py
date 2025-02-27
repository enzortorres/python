import os

palavra_secreta = 'perfume'
palavra_formatada = ['*'] * len(palavra_secreta)
tentativas = 0

while True:
    letra = str(input("Digite uma letra: "))
    tentativas += 1
    
    if len(letra) > 1:
        print("Digite somente uma letra.")
        continue
    
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_formatada[i] = letra

    print(''.join(palavra_formatada))
        
    if '*' not in palavra_formatada:
        os.system('cls')
        print(f"\nParabéns, você conseguiu! A palavra era {palavra_secreta}!")
        print(f"Tentativas: {tentativas}")
        break
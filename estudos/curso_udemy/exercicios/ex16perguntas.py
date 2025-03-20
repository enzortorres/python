from time import sleep
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '4', '5', '6'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['10', '15', '25', '30'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['5', '2', '4', '1'],
        'Resposta': '5',
    }
]

qtd_acertos = 0

while True:
    try:
        for pergunta in perguntas:
            os.system('cls') 
            print(f"Pergunta: {pergunta['Pergunta']}")

            print("\nOpções:")
            for i, opcao in enumerate(pergunta['Opções']):
                print(f"{i + 1}) {opcao}")
            resposta = int(input("Escolha uma opção: ")) - 1

            if pergunta['Opções'][resposta] == pergunta['Resposta']:
                print("\nVocê acertou! ✅\n")
                qtd_acertos += 1
            else:
                print("\nVocê errou! ❌\n")
            sleep(1)
    except:
        print("\n\033[4;31mDigite somente valores válidos\033[0m\n")
        sleep(1)
    else:
        print(f"Você acertou {qtd_acertos} de {len(perguntas)} perguntas!", "Meus parabéns!" if qtd_acertos == 3 else "Foi bem!" if qtd_acertos == 2 else "Melhore!")
    finally:
        if input("Deseja tentar novamente? ") not in 'sSsimSIMSim':
            print("Sistema desligando...")
            break
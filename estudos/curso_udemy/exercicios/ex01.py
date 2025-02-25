nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
contem_espaco = " " in nome
nome = nome.strip()

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    print(f'Seu nome contem espaços? {contem_espaco}')
    nome = nome.replace(' ', '')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A ultima letra do seu nome é "{nome[len(nome) - 1]}"')
else:
    print('Desculpe, você deixou campos vazios.')



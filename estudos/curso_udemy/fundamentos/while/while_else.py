# # ? primeiro while - utilizando else ao final do while

index = 0

while index < 10:
    print(index)
    index += 1
else:
    print("Sem break ele entra no else ao final do while.")
print("\nFim do primeiro while.")

print('\n' + '\033[36m=\033[m' * 30 + '\n')


# # ? segundo while - ao executar um break, nao cai no else


index = 0

while index < 10:
    print(index)
    index += 1
    
    if index == 5:
        break
else:
    print("Com break ele não entra no else ao final do while.")
print("\nFim do segundo while, com break ele não entra no else ao final do while.")

print('\n' + '\033[36m=\033[m' * 30 + '\n')



# # ? terceiro while - um método de utilizar o else

string = 'Testando'
index = 0

while index < len(string):
    if string[index] == ' ':
        break
    
    print(string[index])
    
    index += 1
else:
    print("Não encontrei um espaço na string.")
print("\nFim do terceiro while.")

print('\n' + '\033[36m=\033[m' * 30 + '\n')

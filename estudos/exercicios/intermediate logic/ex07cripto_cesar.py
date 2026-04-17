def cesar_cripto(string: str, chave: int) -> str:
    cripto_string = ""
    for char in string:
        letter_in_ascii = ord(char)
        cripto_letter = letter_in_ascii + chave
        cripto_string += chr(cripto_letter)
    return cripto_string

msg = str(input("Digite uma mensagem: "))
chave = int(input("Digite uma chave (número): "))
cripto_msg = cesar_cripto(msg, chave)

print("Original msg:")
print(msg)

print()

print("Cripto msg:")
print(cripto_msg)
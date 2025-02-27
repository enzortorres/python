numero_str = input("Vou dobrar o número que você digitar: ")

try:
    numero_float = float(numero_str)
    print(f"FLOAT: {numero_float}")
    print(f"O dobro de {numero_str} é {numero_float * 2}")
except Exception as error:
    print(f"Isso não é um número! {error}")
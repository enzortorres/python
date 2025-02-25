try:
    print(1 + '1')
except TypeError as error:
    print(f"Erro de tipagem: {error}")
    
try:
    print('1' + 1)
except TypeError as error:
    print(f"Erro de tipagem: {error}")

try:
    input()
except KeyboardInterrupt:
    print("Programa fechado (CTRL + C)")
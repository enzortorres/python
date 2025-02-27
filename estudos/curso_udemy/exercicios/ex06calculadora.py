oper = 0

while True:
    try:
        num_1 = float(input("Digite um número: "))
        break
    except:
        print("\n\033[31mDigite um valor válido.\033[m\n")
        
while True:
    try:
        num_2 = float(input("Digite outro número: "))
        break
    except:
        print("\n\033[31mDigite um valor válido.\033[m\n")
while True:
    oper = str(input(
'''Qual operação deseja realizar? 
[+] Soma
[-] Subtração
[*] Multiplicação
[/] Divisão
>>> '''
))
    if len(oper) > 1:
        print("\n\033[31mDigite apenas um operador.\033[m\n")
        continue
    if oper in '+-*/':
        break
    else:
        print("\n\033[31mDigite um operador válido.\033[m\n")
        
if oper == '+': 
    result = num_1 + num_2
elif oper == '-':
    result = num_1 - num_2
elif oper == '*':
    result = num_1 * num_2
elif oper == '/':
    if num_1 != 0 and num_2 != 0:
        result = num_1 / num_2
    else:
        print("\n\033[31mNão pode realizar divisão com 0.\033[m\n")
        exit()
print(f"{num_1} {oper} {num_2} = {result}")
''''TDE 1 
Prof Msc. Thereza Gondim 
_________________________________________________________________________ 
1. Peça ao usuário um número inteiro e calcule o dobro desse número. 2. Solicite a largura e a altura de um retângulo e calcule a área. 
3. Peça dois números inteiros e use o operador de igualdade (==) para verificar se eles são iguais. 
4. Peça dois números inteiros e calcule o resto da divisão entre eles usando o operador módulo (%). 
5. Solicite três números e calcule a média aritmética simples deles. 
6. Peça dois números e verifique se o primeiro é maior que 10 e o segundo é menor que 5 usando o operador and.
'''
#EX1
num = int(input("DIgite um valor: "))
print(num * 2)

#EX2
largura = float(input("Digite a largura do retangulo:"))
altura = float(input("Digite a altura do retangulo: "))
print(f"AREA: {largura * altura}")

#EX3
num1 = int(input("Digite um valor:"))
num2 = int(input("Digite outro valor:"))

print(num1 == num2)
#EX4
num3 = int(input("Digite um valor:"))
num4 = int(input("Digite outro valor:"))

print(f"Resto da divisão: num3 % num4")

#EX5
num5 = float(input("Digite um valor:"))
num6 = float(input("Digite outro valor:"))
num7 = float(input("Digite outro valor:"))

soma = num5 + num6 + num7
media = num5 + num6 + num7 /3 

print(f'Media: {media}')

#EX6
num8 = int(input('Digite um valor:'))
num9 = int(input('Digite outro valor:'))

print(num8 > 10 and num9 < 5)




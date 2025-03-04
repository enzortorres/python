import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2 

print(numero_3) # ? Com double-precision floating-point, (0.8)
print(numero3) # ? Sem double-precision floating-point, (0.7999999999999999)
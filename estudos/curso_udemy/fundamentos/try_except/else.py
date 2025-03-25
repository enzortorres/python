
try:
    a = 18
    b = 2
    print(18 / 0)
    print('Linha 1')
    print(a / b)
    print('Linha 2')
    print('Linha 3')
except ZeroDivisionError as e:
    print("Dividiu por zero.", e.__class__.__name__)
except NameError:
    print("Nome b não está definido.")
except (TypeError, IndexError) as error:
    print("TypeError + IndexError")
    print("Exception:", error.__class__.__name__)
except Exception:
    print("Erro desconhecido.")

print("Continuar")
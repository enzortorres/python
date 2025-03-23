string = 'Enzo'
metodo = 'upper'

if hasattr(string, 'upper'):
    print("Existe o método upper")
    print(getattr(string, metodo)())
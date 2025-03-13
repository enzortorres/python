# \r\n -> CRLF
# \n -> LF

def linha():
    print("\n" + "=" * 20, end="\n\n")
    
linha()

print(12, 34, 1011, sep="-", end="\r\n")
print(12, 34, 1011, sep="-", end=" ")
print(12, 34, 1011, sep="-", end="\n")

linha()

print("Meu nome é \"Enzo Ribas\"")
print(r"Meu nome é \"Enzo Ribas\"")
print('Meu nome é "Enzo Ribas"')
print("Meu nome é 'Enzo Ribas'")

linha()

print(type("Enzo"))
print(type(1), type(1.1), type(-10))

linha()

print(10 == 10)
print(10 == 11)
print(type(10 == 10))
print(type(10 == 11))

linha()

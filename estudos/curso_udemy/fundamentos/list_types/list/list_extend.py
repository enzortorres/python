list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
list_a.extend(list_b) # ? Mexe diretamente com a lista A, não pode atribuir em outra variável

print(list_c)
print(list_a)

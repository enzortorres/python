s = 0
for c in range(1, 499, 3):
    print(c+2, end=' ')
    s += c
print('O somátorio de todos os valores foi {}'.format(s))
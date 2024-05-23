print('\033[35m-'*74)
print('{:^82}'.format('\033[4;34mSequencia de Fibonacci'))
print('\033[35m-\033[0m'*74)
n = int(input('\033[33mQuanto termos você quer mostrar?\033[30m '))
t1 = 0 
t2 = 1
print('\033[35m~'*74)
print('\033[34m{} ➝  {}'.format(t1, t2), end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print(' ➝  {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print(' ➝  FIM')
print('\033[35m~'*74)
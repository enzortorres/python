def is_string(func):
    def inner(*args, **kwargs):
        print("Verificando tipo")
        if not all(isinstance(arg, str) for arg in args): # : Verifica se todos os argumentos são strings
            raise TypeError(f'Expected a string, but got a {[type(arg).__name__ for arg in args]} instead') # : Lança um erro ao inserir qualquer variável com um tipo sem ser string
        res = func(*args)
        return res
    return inner

def admin_permission(func):
    ADMIN_USER = 'ENZO'
    global username
    
    def inner(*args):
        print("Verificando permissão")
        if username != ADMIN_USER:
            # raise PermissionError('Do not have acess to that method') # ! O mais certo seria lançar um erro, mas coloquei print para testes
            print('Do not have acess to that method')
            return None
        return func(*args)
    return inner

username = 'ENZO' # : Para simular um login

# ? As decoradoras de cima são executadas primeiro
@admin_permission # > Primeiro checa se tem permissão administradora
@is_string # > Depois chega o tipo do parâmetro
def reverse_string(string):
    return string[::-1]

@admin_permission
@is_string
def concatenate(a, b):
    return a + b

print('\033[32mTeste sendo o usuário ADMIN\033[m')
print("\nFunção reverse_string")
print(reverse_string('Enzo')) # : Aqui a função ocorre normalmente por ter acesso administrativo
print("\nFunção concatenate")
print(concatenate('Enzo', 'Ribas')) # : Aqui a função ocorre normalmente por ter acesso administrativo

print('\n\033[31mTeste sem ser o usuário ADMIN\033[m')
username = 'GUEST' 
print("\nFunção reverse_string")
print(reverse_string('Test')) # : Aqui ele não tem permissão por não ser o usuário "admin"
print("\nFunção concatenate")
print(concatenate('Enzo', 'Ribas')) # : Aqui ele não tem permissão por não ser o usuário "admin"

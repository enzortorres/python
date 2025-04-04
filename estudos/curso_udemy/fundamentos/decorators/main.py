# # | Funções decoradoras e decoradores
# ? Decorar = Adicionar / Remover/ Restringir / Alterar
# ? Funções decoradoras são funções que decoram outras funções
# ? Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
# ? Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func): # ! Função decoradora, criar uma função internada sem execução, somente retornada
    def interna(*args, **kwargs):
        print("Vou te decorar")
        
        for arg in args: # > Dentro da função interna eu posso (Adicionar / Remover/ Restringir / Alterar) antes de dar o resultado
            is_string(arg)
        resultado = func(*args, **kwargs)
        
        print(f"O seu resultado foi {resultado}")
        print("Ok, agora você foi decorada")
        
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("Param deve ser uma string")


invertida = inverte_string('123')
print(invertida)
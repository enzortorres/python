"""
    | Positional-Only Parameters (/) e Keyword-Only Arguments (*)
    ? *args (ilimitado de argumentos posicionais)
    ? **kwargs (ilimitado de argumentos nomeados)
    
    | Positional-only Parameters (/) - Tudo antes da barra deve ser APENAS posicional.
    ? PEP 570 - Python Positional-Only Parameters
    > https://peps.python.org/pep-0570/
    
    | Keyword-Only Arguments (*) - * sozinho NÃO SUGA valores.
    ? PEP 3102 - Keyword-Only Arguments
    > https://peps.python.org/pep-3102/
"""

def soma(x, y, /, a, b): # > Antes do "/" todos argumentos obrigatóriamente precisam ser posicionais, depois, volta ao padrão
    print(x + y)

soma(1, 2, 10, b=10)

def soma(x, y, *, a): # > Depois do "*" todos argumentos obrigatóriamente precisam ser nomeados, antes, continua no padrão
    print(x + y + a)

soma(1,2, a=10)

def soma(x, y, /, *, a): # > Antes da "/" obrigatóriamente precisam ser posicionais, pós "*" precisam ser nomeados
    print(x + y + a)

soma(1,2, a=10)
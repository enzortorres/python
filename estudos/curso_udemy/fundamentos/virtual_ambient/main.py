"""
    | Ambientes virtuais em Python (venv)
    ? Um ambiente virtual carrega toda a sua instalaçãodo Python para uma pasta no caminho escolhido.
    ? Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.
    ? venv é o módulo que vamos usar para criar ambientes virtuais.
    ? Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são: 
    > venv env .venv .env
"""

# ! Como criar ambientes virtuais
# > Abra a pasta do seu projeto no terminal
# python -m venv (nome do ambiente virtual, "venv" é o mais comum) # > Para criar o ambiente virtual
# ./venv/Scripts/activate # > Para ativar o ambiente virtual
# deactivate # > Para desativar o ambiente virtual

# ! Como instalar pacotes e bibliotecas
# pip install pymysql # > Para instalar pacotes e bibliotecas
# pip uninstall pymysql # > Ele pergunta se realmente deseja desinstalar a biblioteca
# pip uninstall pymysql -y # > Aqui ele não pergunta, desinstala direto

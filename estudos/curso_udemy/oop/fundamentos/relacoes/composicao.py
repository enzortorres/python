"""
    | Relações entre classes: associações, agregação e composição
    ? Composição é uma especialização da agregação.
    ? Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas. 
"""
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) # > instânciar a classe dentro de outra classe (Garbage Collector)
        # ? Quando o cliente deixar de existir, a instância também vai deixar de existir.
        
    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f"{endereco.rua}, {endereco.numero}")
    
    def __del__(self):
        print('APAGANDO', self.nome)
    
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('APAGANDO', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 23)

endereco_externo = Endereco('Avenida Saudade', 1234) # Adicionando endereço de forma externa, ao deletar cliente, o endereço não é apagado, 
# Cliente vai ser apagado na linha 44, porém o endereço só é deletado com o Collect Garbage

cliente1.inserir_endereco_externo(endereco_externo)

cliente1.listar_enderecos()

del cliente1 

print("############# AQUI TERMINA MEU CÓDIGO")
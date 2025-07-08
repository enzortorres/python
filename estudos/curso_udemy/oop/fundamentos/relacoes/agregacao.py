"""
    | Relações enre classes: associações, agregação e composição
    > Agregação - tem
    ? Agregação é uma forma mais especialiazada de associação entre dois ou mais objetos.
    ? Cada objeto terá seu ciclo de vida independente.
    ? Geralmente é uma relação de um para muitos, onde um objeto tem um ou mais objetos.
    ? Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.
    ? (Existem controvérsias sobre as definições de agregação).
    
    ex: Carro e roda, ambos vivem sem o outro, mas o carro necessita da roda para funcionar perfeitamente.
"""
class Carrinho:
    def __init__(self):
        self._produtos = []
        
    def total(self):
        return f'R${sum([p.preco for p in self._produtos]):.2f}'.replace('.', ',')
    
    def inserir_produtos(self, *produtos):
        # > Os 3 funcionam para esse caso
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1,p2 = Produto('Caneta', 1.20), Produto('Camiseta', 30)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())

class Carro:
    def __init__(self, placa, modelo, cor):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor
        self._rodas = []
    
    def inserir_roda(self, *modelos_pneus):
        if len(modelos_pneus) > 4:
            print('Só pode colocar 4 rodas no carro.')
            return
        
        if len(self._rodas) == 4:
            print('O carro já possuí 4 rodas.')
            return
        self._rodas.extend(modelos_pneus)
    
    def dados_carro(self):
        modelos_pneus = [p for p in self._rodas]
        print(f'Placa: {self.placa}')
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Modelos dos pneus:', *modelos_pneus, sep="\n")
    
    def andar(self):
        if len(self._rodas) < 4:
            print('Carro não consegue andar.')
            return
        print(f'{self.modelo} está andando.')

taos = Carro('ABC-1234', 'Taos 2025', 'Cinza')
taos.inserir_roda('Pneu 215/50R17 Michelin Primacy 4+ XL 95W', 'Pneu 215/50R17 Michelin Primacy 4+ XL 95W', 'Pneu 215/50R17 Michelin Primacy 4+ XL 95W', 'Pneu 215/50R17 Michelin Primacy 4+ XL 95W')
taos.dados_carro()
taos.andar()
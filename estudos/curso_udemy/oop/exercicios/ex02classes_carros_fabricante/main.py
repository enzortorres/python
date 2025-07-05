class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
    
    def listar_dados(self):
        print(
            f"Carro: {self.nome}",
            f"Motor: {self._motor.nome}",
            f"Fabricante: {self.fabricante.nome}", sep="\n"
        )
        print()

class Motor: 
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

volkswagen = Fabricante('Volkswagen')
fiat = Fabricante('Fiat')
ford = Fabricante('Ford')
motor_1_0 = Motor('1.0')
motor_2_0 = Motor('2.0')


taos = Carro('Taos')
taos.motor = motor_2_0
taos.fabricante = volkswagen


fusca = Carro('Fusca')
fusca.motor = motor_1_0
fusca.fabricante = volkswagen


uno = Carro('Uno')
uno.motor = motor_1_0
uno.fabricante = fiat


focus = Carro('Focus')
focus.motor = motor_2_0
focus.fabricante = ford


taos.listar_dados()
fusca.listar_dados()
focus.listar_dados()
uno.listar_dados()
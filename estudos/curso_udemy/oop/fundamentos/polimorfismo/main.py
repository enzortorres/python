"""
    | Polimorfismo - Python Orientado a Objetos
    ? Polimorfismo é o princípio que permite que classes derivadas (que herdam de uma superclasse) de uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.
    ? Assinatura do método = mesmo nome e quantidade de parâmetros (retorno que não faz parte da assinatura).
    
    : Opnião + princípios que contam:
        > Assinatura do método: nome, parâmetros e retornos iguais
        > SO"L"ID
        > Princípio da substituição de liskov
    
    ? Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.
    ? Sobrecarga de métodos (overload) 🐍 = ❌
    ? Sobreposição de métodos (override) 🐍 = ✅
"""
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool: # ? typehinting ( -> bool), serve para indicar para os devs oque esse método deve retornar
        ...
        
class NotificacaoViaEmail(Notificacao):
    def enviar(self) -> bool: 
        print('Enviado pelo email:', self.mensagem)
        return True

class NotificacaoViaSMS(Notificacao):
    def enviar(self) -> bool: 
        print('Enviado pelo SMS:', self.mensagem)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    
    if notificacao_enviada:
        print('Notificação enviada.')
    else:
        print('Notificação NÃO enviada.')

notificacao_email = NotificacaoViaEmail('Testando e-mail')
notificar(notificacao_email)

print()

notificacao_sms = NotificacaoViaSMS('Testando SMS')
notificar(notificacao_sms)
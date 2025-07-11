"""
    | Abstração - Python Orientado a Objetos
    ? É o ato de esconder a complexidade e mostrar apenas o necessário.
    ? Usamos para definir uma "interface comum" que deve ser implementada por outras classes.
    
    > Classe abstrata:
        : É uma classe que serve como modelo e "não deve ser instanciada" diretamente.
        : Pode conter métodos com implementação (concretos) ou sem (abstratos).
        : Em Python, pode ser feita de forma "manual" com `raise NotImplementedError`
        : Ou de forma formal com `abc.ABC` e `@abstractmethod`
    
    ex:
        > class Log:
        >    def log(self, msg):
        >        raise NotImplementedError('Implemente o método log')
        
        > class LogFileMixin(Log):
        >   def log(self, msg):
        >      print(msg)
    
    ex:
        > import abc
        > class Log(abc.ABC):
        >   @abc.abstractmethod
        >   def log(self, msg):
        >       ...
    
    ? Classes que herdam de uma classe abstrata "devem implementar" os métodos abstratos.
    ? Se não implementar, o Python lança erro ao tentar instanciar a classe.
    
    > Dica:
        : Ideal para garantir que subclasses sigam um contrato (interface).
        : Muito usado com mixins, padrões de projeto e arquitetura limpa.
"""
class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log')

class LogFileMixin(Log):
    def log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def log(self, msg):
        print(msg)

if __name__ == '__main__':
    l = LogFileMixin()
    l.log('Qualquer coisa')
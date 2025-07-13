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
from pathlib import Path

BASE_DIR = Path(__file__).parent / 'log.txt'
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')
        
    def log_sucess(self, msg):
        self._log(f'Sucess: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log: ', msg_formatada)
        with open(BASE_DIR, 'a') as file:
            file.write(msg_formatada)
            file.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_sucess('que legal')
    
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_sucess('que legal')
    print(BASE_DIR)
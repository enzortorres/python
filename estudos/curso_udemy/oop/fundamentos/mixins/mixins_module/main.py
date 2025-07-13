"""
    | Mixins - Python Orientado a Objetos
    ? Mixin é uma classe feita "para ser herdada", mas "não para ser instanciada"
    ? Ela adiciona funcionalidades extras (comportamentos), sem formar uma hierarquia de "é um" (is-a).
    
    ? São usadas com herança múltipla.
    ? O foco é "reutilização de código", não generalização.`
    
    > Regras para um Mixin:
        : Não deve ser usada sozinha (não deve ser instanciada diretamente)
        : Deve ter responsabilidade única (ex: apenas log, salvar, validar, etc)
        : Nome geralmente termina com 'Mixin' por convenção (ex: LogMixin, JsonMixin)
    
    ex:
        > class LogMixin:
        >     def log(self, msg):
        >         print(f'[LOG]: {msg}')

        > class MinhaClasse(LogMixin):
        >     pass
    
    > Você pode combinar vários Mixins numa classe:
        ex: MinhaClasse(Base, LogMixin, SaveMixin, ValidateMixin)
    
    ? Mixins são uma forma de aplicar composição com herança.
    ? Úteis para separar responsabilidades e evitar códigos duplicado.
"""

from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('qualquer coisa')
lp.log_sucess('que legal')

lf = LogFileMixin()
lf.log_error('qualquer coisa')
lf.log_sucess('que legal')
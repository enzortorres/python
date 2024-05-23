import emoji
from datetime import date
from time import sleep
ano = date.today().year
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('FELIZ ANO NOVO :fireworks:!!! QUE {} SEJA REFLETO DE CONQUISTAS, FELICIDADES E TUDO QUE HÁ DE BOM!!!').format(ano+1))
"""
    | Sets - Conjuntos em Python (tipo set)
    > Conjuntos são ensinados na matemática
    > https://brasilescola.uol.com.br/matematica/conjunto.htm
    > Representados graficamente pelo diagrama de Venn
    > Sets em Python são mutáveis, porém aceitam apenas
    > tipos imutáveis como valor interno.
"""

# ! Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set('Enzo') 
print(s1)

s1 = set()  # vazio
s1 = {'Enzo', 1, 2, 3}  # com dados
print(s1)

# ! Sets são eficientes para remover valores duplicados de iteráveis.
# ? Seus valores serão sempre únicos;
# ? Não aceitam valores mutáveis;
# ? não tem índexes;
# ? não garantem ordem;
# ? são iteráveis (for, in, not in)

lista = [1,2,3,3,3,3,3,3,1]
s2 = set(lista)
print(s2)

for num in s2:
    print(num)

# ! Métodos úteis:
# ? add, update, clear, discard

s3 = set()
s3.add('Enzo')
print(s3)
s3.add(1)
print(s3)
s3.update(('Olá mundo',))
# s3.clear()
print(s3)
s3.discard('Enzo')
print(s3)

# ! Operadores úteis:
# ? união | união (union) - Une
# ? intersecção & (intersection) - Valores presentes em ambos
# ? diferença - Valores presentes apenas no set da esquerda
# ? diferença simétrica ^ - Valores que não estão em ambos

s4 = {1,2,3}
s5 = {2,3,4}

s6 = s4 | s5 # > União dos sets
print(s6) # : {1,2,3,4}

s6 = s4 & s5 # > Intersecção dos sets (Presentes em ambos os sets)
print(s6) # : {2,3}

s6 = s4 - s5 # > Os valores que estão presentes apenas no set da esquerda
print(s6) # : {1}

s6 = s5 - s4 # > Os valores que estão presentes apenas no set da direita
print(s6) # : {4}

s6 = s5 ^ s4 # > Os valores que NÃO estão presentes em ambos
print(s6) # : {1,4}

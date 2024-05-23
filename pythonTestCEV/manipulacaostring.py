#Aula de Número 8, como manipular texto!
frase = 'Curso em vídeo python'

#Fatiamento de string
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
#Analisar uma string
print(len(frase))
print(frase.count('o',0,13))
print(frase.find('deo')) 
print(frase.find('Android'))
print('Curso' in frase)
#Transformação de string
print(frase.replace('python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
#Divisão de string
print(frase.split())
#Junção de string
print('-'.join(frase))

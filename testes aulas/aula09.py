#testes aula 09 - Manipulando Strings

#Fatiamento
# as contagens de caracteres começa de 0 e conta os espaços.///ex.: 0,1,2,3,4,5...

frase = 'Curso em Vídeo Python'
print(frase[9]) #escreva o caractere 9
print(frase[9:13]) #o : significa intervalo. As [] significa que é uma lista.
print(frase[9:21]) #escreva do 9 ao 21
print(frase[9:21:2]) # escreva do 9 ao 21 pulando de 2 em 2 caracteres
print(frase[:5]) #escreva do início até o caractere 5
print(frase[15:]) #escreva do caractere 15 até o fim
print(frase[9::3]) #escreva do 9 até o fim pulando de 3 em 3 caracteres

#Análise

frase = 'Curso em Vídeo Python'
print(len(frase)) #len é o comprimento da frase
print(frase.count('o')) #conta quantos 'o's tem na frase
print(frase.count('o',0,13)) #conta quantos 'o's tem entre 0 e 13
print(frase.find('deo')) #diz a posição de 'deo' na frase
print('Curso' in frase) #operador que diz se existe a palavra 'Curso' dentro da frase e responde True ou False

#Transformação

frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android')) #substitui a palavra Phyton por Android
print(frase.upper()) #bota tudo em maiúsculo/// parênteses vazios pq é um método
print(frase.lower()) #bota tudo em minúsculo
print(frase.capitalize()) #só o primeiro caractere em maiúsculo
print(frase.title()) #bota o primeiro caractere de cada palavra em maiúsculo

frase = '   Aprenda Python  '
print(frase.strip()) #remove todods os espaços vazios inúteis
print(frase.rstrip()) #remove os espaços vazios inúteis da direita
print(frase.lstrip()) #remove todos os espaços vazios inúteis da esquerda

#Divisão ATENÇÃO: estudar splits

frase = 'Curso em Vídeo Python'
dividido = frase.split()
conte = frase.count('o',0, 3)
print(frase.split()) # retorna ['Curso', 'em', 'Vídeo', 'Python'] separa em listas, cortando os espaços. cada palavra corresponde a um caractere
print('-'.join(frase)) #separa cada caractere com um -
print(frase.splitlines()) #a frase fica em uma lista
print(len(frase.splitlines())) #comprimento da frase em lista
print(dividido[0])

print(frase.split(' ',2)) #retorna ['Curso', 'em', 'Vídeo Python']





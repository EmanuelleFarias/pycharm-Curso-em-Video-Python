''' Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''
f = (input('Digite uma frase: '))
fse = f.strip().replace(' ','') #frase sem espaço
inv = ''.join(reversed(f)) #outra opção de frase invertida
fi = f[::-1] #frase invertida (significa frase[:: ( intervalo do começo ao fim) - 1 (de trás pra frente)]
fsei = fse[::-1] #frase sem espaço invertida
print(f)

print('O inverso da frase {} é {}.'.format(fse, fsei))
if fsei == fse:
    print('A frase é um palíndromo!!!')
else:
    print('A frase não é um palíndromo.')


# usando o for
frase = str(input('Digite uma frase: ')).strip().upper() #tira os espaços do fim e do começo e bota tudo em maíusculo
palavras = frase.split() #separa em palavras (listas)
junto = ''.join(palavras)# junta as palavras sem espaço
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!!!')
else:
    print('A frase digitada não é um palíndromo.')


for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
tup = (num1,num2,num3,num4)
cont = 0
pares = []
print(sorted(tup))
if num1 %2 != 0 and num2 %2 != 0 and num3 %2 != 0 and num4 %2 != 0:
    print('Não foi digitado nenhum número par.')
if 9 in tup:
    print('O número 9 apareceu',tup.count(9),'vez(es).')
else:
    print('O número 9 não foi digitado nenhuma vez.')
if 3 in tup:
    print('O primeiro número 3 foi digitado na',tup.index(3)+1,'posição.')
else:
    print('O número 3 não foi digitado nenhuma vez.')
if num1 %2 ==0:
    cont+= 1
    pares.append(num1)
if num2 % 2 == 0:
    cont += 1
    pares.append(num2)
if num3 % 2 == 0:
    cont += 1
    pares.append(num3)
if num4 % 2 == 0:
    cont += 1
    pares.append(num4)
print(f'Foram digitados {cont} números pares: {pares}.')




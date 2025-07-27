'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:

a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
b) quais foram os números pares
'''
tup_num = ()
lis_num = []
for v in range(0,4):
    valor = int(input('Digite um número: '))
    lis_num.append(valor)
tup_num = tuple(lis_num)
print(tup_num)

if 9 in tup_num:
    print(f'\n⫸ O número 9 apareceu {tup_num.count(9)} vez(es).')
else:
    print('⫸ O número 9 não foi digitado nenhuma vez.')

if 3 in tup_num:
    print(f'⫸ O primeiro número 3 apareceu na posição {tup_num.index(3)+1}.')
else:
    print('⫸ O número 3 não foi digitado nenhuma vez.')

print(f'⫸Foram digitados os seguintes números pares:', end=' ')
'''for v in tup_num:
    if v % 2 == 0:
        print(f'{v}',end=' ')'''
print(', '.join(str(v) for v in tup_num if v % 2 == 0))

print('')


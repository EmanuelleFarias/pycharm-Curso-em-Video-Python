#maior e menor peso em uma sequência
''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''
pma = 0
pme = 0
for pess in range(1,6):
    p = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1: # se o primeiro laço (primeira leitura for ==1, tanto o maior quanto o menor é p)
        pma = p
        pme = p

    if p > pma:
        pma = p
    elif p < pme:
        pme = p
print('')
print('O maior peso é {}kg.'.format(pma))
print('O menor peso é {}kg.'.format(pme))

'''#outro jeito
lista = [] #lista vazia
for c in range(1,6):
    p = float(input('Peso da {}ª pessoa: '.format(c)))
    lista += [p] #vai acrescentar os pesos na lista
print('')
print('O maior peso foi: {}kg.'.format(max(lista))) #vai buscar o maior peso
print('O menor peso foi {}kg.'.format(min(lista))) #vai buscar o menor peso'''


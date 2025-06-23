'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

totalcompra = 0
maisqm = 0
listaprod = []
listapreço = []
while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$ '))
    totalcompra += p
    listaprod.append(n)
    listapreço.append(p)
    if p > 1000:
        maisqm += 1
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? (S/N): ')).strip().lower()[0]
    if resp == 'n':
        break

menor_preco = min(listapreço)
indice_menor = listapreço.index(menor_preco)
prod_mais_barato = listaprod[indice_menor]

print(f'O total geral das compras foi de R${totalcompra}.')
print(f'{maisqm} produtos custaram mais que R$1.000,00.')
print(f'O produto mais barato foi {prod_mais_barato} por R${menor_preco:.2f}.')

#outro jeito aula

'''total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço < 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? (S/N): ')).strip().lower()[0]
    if resp == 'n':
        break
print(f'O total geral das compras foi de R${total:.2f}.')
print(f'{totmil} produtos custaram mais que R$1.000,00.')
print(f'O produto mais barato foi {barato} por R${menor:.2f}.')'''


lanche = ['suco', 'hamburguer', 'suco', 'pizza', 'pudim', 'suco']
print(lanche)


lanche.append('pancho') # acrescenta no final da lista
print(lanche)

lanche.insert(0,'refri') #inserta (não substitui) na posição que eu quiser. neste caso, na posição 0 o refri
print(lanche)

lanche.pop(3) #apagou o item da pos 3 (suco)
print(lanche)

lanche.pop() #apaga o ultimo item
print(lanche)

lanche.__delitem__(3)#apagou o item da pos 3 (pizza)
print(lanche)

lanche.remove('suco')#apagou o item suco ATENÇÃO: SE TEM MAIS DE UM, ELE REMOVE A PRIMEIRA OCORRENCIA, ou seja, o primeiro suco.
print(lanche)

if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(4,11))
print(valores)

lista = [8,2,5,4,9,3,0]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

print(len(lista))

print('{:=^60}'.format(' TESTES '))
print()

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

for posicao, valor in enumerate(valores):
    print(f'\nNa posição {posicao} encontrei o valor {valor}')
print('Cheguei ao final da lista.')

print()
'''valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for posicao, valor in enumerate(valores):
    print(f'\nNa posição {posicao} encontrei o valor {valor}')
print('Cheguei ao final da lista.')'''


print('---'*60)

a = [2,3,4,7]
b = a # isso interliga as duas listas
b = a[:] # aqui copia a lista sem interligar. O[:] significa 'tudo'
b[2] = 8
print(f'Lista A : {a}')
print(f'Lista B: {b}')


print('----- CONTANDO ELEMENTOS REPETIDOS -----')
print(c.count(5)) #conta elementos repetidos na tupla
print('----- INDEX dizendo a posição -----')
print(c.index(2))
print('----- INDEX dizendo a posição a partir de um ponto (qdo os itens se repetem -----')
print(c.index(2,1))


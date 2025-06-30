'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.'''

t1 = int(input('digite o primeiro termo da PA: ')) #primeiro termo
r = int(input('Digite a razão da PA: ')) #razão
termo = t1
cont = 1
while cont <= 10:
    print('{} →'.format(termo), end = ' ')
    termo += r
    cont += 1
print('fim')


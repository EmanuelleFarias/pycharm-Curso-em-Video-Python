'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''
tab = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Athlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba','Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Os cinco primeiros colocados são: {tab[:5]}')
print(f'Os últimos quatro colocados são: {tab[-4:]}')
print(f'A tabela em ordem alfabética é: {sorted(tab)}')
print('A Chapecoense está na',tab.index('Chapecoense')+1,'posição.')


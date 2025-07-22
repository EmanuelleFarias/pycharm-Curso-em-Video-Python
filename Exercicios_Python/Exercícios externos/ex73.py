'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense
'''

times = ('Cruzeiro', 'Flamengo', 'Bragantino', 'Palmeiras', 'Botafogo',
         'Bahia', 'Mirassol', 'Fluminense', 'Atlético-MG', 'Corinthians',
         'Ceará', 'Internacional', 'Grêmio', 'São Paulo', 'Vitória',
         'Vasco', 'Santos', 'Juventude', 'Fortaleza', 'Sport')
print('⏔' *45)
print(f'Times do Brasileirão:\n {times}')
#for t in times:
   # print(t)
print('⏔' *45)
print(f'Os cinco primeiros colocados são:\n {times[:5]}')
#for t in times:
  # print(times[:5])
  # break
print('⏔' *45)
print(f'Os quatro últimos colocados são:\n {times[-4:]}')
#for t in times:
  #print(times[-4:])
  #break
print('⏔' *45)
print(f'Times em ordem alfabética:\n {sorted(times)}')
print('⏔' *45)
print(f"O Palmeiras está na {times.index('Palmeiras')+1}ª posição.")

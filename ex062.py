'''
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

from time import sleep

t1 = int(input('digite o primeiro termo da PA (para finalizar digite 0): ')) #primeiro termo
r = int(input('Digite a razão da PA: ')) #razão
#termo = t1
cont = 1 #começa com 1 pq já temos o primeiro termo da PA
total = 0 # pq ainda não comecou a calcular
mais = 10 # pq é o ponto de partida (primeiro queremos que mostre os 10 primeiros termos)
while mais != 0: #enquanto o mais for diferente de zero ( ele já é diferente de zero pq ele é 10), ou seja, agora (True)↲
    total = total + mais # ↳ o total será igual a ele mesmo + mais. Ou seja, começa já com o total 10 ( 0 + 10 = 10)
    while cont <= total: # enquanto o contador for menor ou igual ao total (10)↲
        print('{} →'.format(t1), end = ' ') # ↳ mostre o termo ↲
        t1 += r # ↳ sendo que o termo é ele mesmo + a razão
        cont += 1 # o contador vai acrescentando um a medida que vai crescendo (1, 2, 3, 4...)
    print('pausa')
    sleep(1)
    print('')
    mais = int(input('Quantos termos a mais você deseja receber? (para finalizar digite 0) '))
    print('')
print('ok. Tchauzinho!!! Processo finalizado com {} termos mostrados.'.format(total))

'''num = int(input(f'Ingresa o primeiro termo: '))
diferencia = int(input(f'Ingresa a diferença comum: '))

print('---')
print('PROGRESSÃO ARITMÉTICA:')
print(num, end=' ') # Mostra o primeiro termo
termo_atual = 1 # Usamos termo_atual para contar quantos termos já foram exibidos

# Loop inicial para exibir os 10 primeiros termos
while termo_atual < 10:
    num += diferencia
    print(num, end=' ')
    termo_atual += 1

print('...') # Indica que a progressão continua.......

# Loop para perguntar ao usuário se quer mais termos
mais_termos = 1 # Inicializa com 1 para entrar no loop
while mais_termos != 0:
    print('\n---') # Adiciona uma linha para melhor visualização
    mais_termos = int(input('Quantos termos você quer mostrar a mais? (0 para encerrar): '))

    if mais_termos < 0:
        print("Por favor, digite um número positivo de termos.")
        continue # Volta para o início do loop

    if mais_termos == 0:
        print('Programa encerrado.')
        break # Sai do loop se o usuário digitar 0

    # Exibe os termos adicionais
    termos_exibidos_agora = 0
    while termos_exibidos_agora < mais_termos:
        num += diferencia
        print(num, end=' ')
        termos_exibidos_agora += 1
        termo_atual += 1 # Continua contando o total de termos exibidos
    print('...') # Indica que a progressão continua'''

termino_n= int(input('Ingresa el número: '))
diferencia=int(input('Ingresa la dif. común de la P.A.: '))

cont=1
total_t=0
pasos=10
while pasos!=0:
  total_t = total_t + pasos
  while cont<=total_t:
    print(termino_n, end=' ')
    termino_n += diferencia
    cont += 1
  pasos = int(input('cuantos más?:  '))
print(total_t)
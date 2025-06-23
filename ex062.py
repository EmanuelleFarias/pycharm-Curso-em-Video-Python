from time import sleep

t1 = int(input('digite o primeiro termo da PA (para finalizar digite 0): ')) #primeiro termo
r = int(input('Digite a razão da PA: ')) #razão
termo = t1
cont = 1 #começa com 1 pq já temos o primeiro termo da PA
total = 0 # pq ainda não comecou a calcular
mais = 10 # pq é o ponto de partida (primeiro queremos que mostre os 10 primeiros termos)
while mais != 0: #enquanto o mais for diferente de zero ( ele já é diferente de zero pq ele é 10), ou seja, agora (True)↲
    total = total + mais # ↳ o total será igual a ele mesmo + mais. Ou seja, começa já com o total 10 ( 0 + 10 = 10)
    while cont <= total: # enquanto o contador for menor ou igual ao total (10)↲
        print('{} →'.format(termo), end = ' ') # ↳ mostre o termo ↲
        termo += r # ↳ sendo que o termo é ele mesmo + a razão
        cont += 1 # o contador vai acrescentando um a medida que vai crescendo (1, 2, 3, 4...)
    print('pausa')
    sleep(1)
    print('')
    mais = int(input('Quantos termos a mais você deseja receber? '))
    print('')
print('ok. Tchauzinho!!! Processo finalizado com {} termos mostrados.'.format(total))
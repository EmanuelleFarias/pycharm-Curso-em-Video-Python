from calendar import isleap
from time import sleep
from datetime import date
from emoji import emojize
print('')
a = int(input('Digite o ano que deseja consultar. Caso seja o ano atual, digite 0. '))
print('')
aa = 'Analisando'
print('{:~^20}'.format(aa))
sleep(2)
print('')
if a == 0:
    a = date.today().year
if isleap(a) is True:
    print(emojize("O ano de {} é bissexto!!! :call_me_hand:📆".format(a)))
else:
    print(emojize('O ano de {} não é bissexto.:thumbs_down:📆'.format(a)))

    #outro jeito
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0: # ano divisível por 4 é bissexto e ano não divisível por 100 ou ano divisível por 400
    print(emojize("O ano de {} é bissexto!!! :call_me_hand:📆".format(a)))
else:
    print(emojize('O ano de {} não é bissexto.:thumbs_down:📆'.format(a)))






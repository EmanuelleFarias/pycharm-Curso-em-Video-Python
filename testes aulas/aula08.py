#import math como usar raiz quadrada

import math #importa toda a biblioteca de matemática
num = int(input('digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}.'.format(num,raiz))

#duas casas decimais {:.2f} e arrendodado pra cima math.ceil(raiz)
print('A raiz de {} é igual a {:.2f}.'.format(num,math.ceil(raiz)))

#arredondado pra baixo
print('A raiz de {} é igual a {:.2f}.'.format(num,math.floor(raiz)))

#importando funcionalidade específica da biblioteca math

from math import sqrt, floor
num = int(input('digite um número:'))
raiz = sqrt(num)
print('A raiz de {} é {}.'.format(num,floor(raiz)))




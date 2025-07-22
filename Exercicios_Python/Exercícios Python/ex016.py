num = float(input('digite um número:'))
intt = int(num)
print('a parte inteira é {}.'.format(intt))
print('')#para dar espaço entre linhas
import math
num = float(input('digite um número de novo:'))
print('a parte inteira de {} é {}.'.format(num, math.trunc(num)))
print('')
from math import trunc
num = float(input('digite um numero outra vez:'))
print('a parte inteira de {} é {}.'.format(num, trunc(num)))


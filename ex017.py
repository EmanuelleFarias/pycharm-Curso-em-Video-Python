from math import hypot
co = float(input('cateto oposto:'))
ca = float(input('cateto adjacente:'))
h = hypot(co,ca)
print('A hipotenusa é {}.'.format(h))

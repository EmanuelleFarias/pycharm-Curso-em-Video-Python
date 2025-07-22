import math
a = float(input('ângulo:'))
an = math.radians(a)
s = math.sin(an)
c = math.cos(an)
t = math.tan(an)
print(' O seno, cosseno e tangente do ângulo {:.2f}° são, respectivamente, {:.2f}, {:.2f} e {:.2f}.'.format(s,c,t,a))

from math import radians, sin, cos, tan
a = float(input('angulo 2:'))
s = sin(radians(a))
print('o seno é',s)
c = cos(radians(a))
print('o coseno é',c)
t = tan(radians(a))
print('a tangente é',t)



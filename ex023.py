num = int(input('digite um número: '))
u = num//1%10 #% é módulo, que é o resto da divisão. neste caso, por 10, que é pra ficar um dígito só. se botar 100, ficam dois dígitos (45)
d = num//10%10
c = num//100%10
m = num//1000%10
print('a unidade é:{}.'.format(u))
print('a dezena é:{}.'.format(d))
print('a centena é:{}'.format(c))
print('a milhar é:{}'.format(m))


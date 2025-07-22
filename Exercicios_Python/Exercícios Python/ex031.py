v = float(input('qual a distância da sua viagem? '))
p1 = v * 0.50
p2 = v * 0.45
print('')
if v <=200:
    print('O valor da sua passagem é R${:.2f}.'.format(p1))
else:
    print('O valor da sua passagem é R${:.2f}.'.format(p2))

#outro jeito >>> if simplificado
p = v *0.50 if v <= 200 else v * 0.45
print('O valor da sua passagem é R${:.2f}.'.format(p))
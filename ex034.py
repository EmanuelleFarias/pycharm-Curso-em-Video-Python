from emoji import emojize
from time import sleep
s = float(input('Informe o seu salário: '))
a1 = s*10/100 # para salarios >1250,00
a2 = s*15/100 # para salários =<1250,00
print('')
print('calculando...🥸🤏🧮')
print('')
sleep(2)
if s > 1250.00:
    print('O seu novo salário é de R${:.2f}🤑💰'.format(s+a1))
else:
    print('O seu novo salário é de R${:.2f}🤑💰'.format(s+a2))



#Calculando  alistamento militar
from datetime import date
ah = date.today().year #ano de hoje
a = int(input('Ano de nascimento: ')) #ano
i = ah - a # idade
aa = a +18 # ano de alistamento
tf = aa - ah # tempo que falta para se alistar
tf2 = ah - aa
print('Quem nasceu em {} tem {} anos em 2025.'.format(a,i))
if i < 18:
    print('Faltam {} anos para o seu alistamento. \nVocê deve se alistar em {}.'.format(tf, aa))
elif i > 18:
    print('Seu alistamento foi há {} anos, em {}.'.format(tf2, aa))
else:
    print('Você deve se alistar este ano!')
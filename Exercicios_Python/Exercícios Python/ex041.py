from datetime import date
aa = date.today().year
an = int(input('Ano de nascimento: '))
i = aa - an
print('O atleta tem {} anos.'.format(i))
if i <= 9:
    print('A sua categoria é MIRIM.')
elif 9 < i <= 14: # pode colocar só elif i <= 14
    print('A sua categoria é INFANTIL.')
elif 14 < i <= 19: # pode colocar só elif i <= 19
    print('A sua categoria é JUNIOR.')
elif 19 < i <= 25: # pode colocar só elif i <= 25
    print('A sua categoria é SÊNIOR.')
elif i > 25: # pode colocar else
    print('A sua categoria é MASTER.')


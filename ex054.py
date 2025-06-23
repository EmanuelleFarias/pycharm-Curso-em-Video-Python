''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
import datetime
aa = datetime.date.today().year # ano atual
sma = 0 # soma dos maiores
sme = 0 # soma dos menores
for pess in range(1,8):
    a = int(input('Ano de nascimento da {}ª pessoa: '.format(pess)))
    i = aa - a # idade
    if i >= 21:
        sma = sma + 1
    else:
        sme = sme + 1
print('A quantidade de pessoas maiores de idade é de {}.'.format(sma))
print('A quantidade de pessoas menores de idade é de {}.'.format(sme))


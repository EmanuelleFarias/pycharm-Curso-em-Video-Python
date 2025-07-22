#Aprovando empréstimo habitação
c = float(input('Qual o valor da casa que deseja financiar? R$'))
s = float(input('Qual o valor do seu salário? R$'))
a = int(input('Em quantos deseja pagar o financiamento? '))
p = c/a/12
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação é de R${:.2f}.'.format(c,a,p))
if p <= s*30/100:
    print('Empréstimo LIBERADO!')
else:
    print('Empréstimo NEGADO!')

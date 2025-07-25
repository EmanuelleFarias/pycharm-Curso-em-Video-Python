#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

populacao_menor = int(input('Informe a menor população: '))
populacao_maior = int(input('Informe a maior população: '))
taxa_menor = float(input('Taxa da menor população: '))
taxa_maior = float(input('Taxa da maior população: '))

'''cresc_1 = populacao_1 * taxa_1/100
cresc_2 = populacao_2 * taxa_2/100'''
anos = 0

while populacao_menor < populacao_maior:
    populacao_menor += populacao_menor*taxa_menor/100
    populacao_maior += populacao_maior*taxa_maior/100
    anos += 1

print(f'A quantidade de anos é {anos}')
print(populacao_menor)
print(populacao_maior)
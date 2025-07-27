#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

qtde = input('Quantos números deseja inserir? ')
while not qtde.isdigit():
    print('Valor inválido.')
    qtde = input('Quantos números deseja inserir? ')
qtde = int(qtde)
print('\nOk! Vamos começar!')

conjunto = []
soma = 0
for n in range(1, qtde+1):
    num = input(f'Digite o {n} número → ')

    while not num.isdigit():
        print('Valor inválido.')
        num = input(f'Digite o {n} número → ')
    num = int(num)
    conjunto.append(num)
    soma += num

print(f'\nO conjunto formado foi: {conjunto}')
print(f'O maior número é {max(conjunto)}.')
print(f'O menor número é {min(conjunto)}.')
print(f'A soma de todos os números é {soma}.')
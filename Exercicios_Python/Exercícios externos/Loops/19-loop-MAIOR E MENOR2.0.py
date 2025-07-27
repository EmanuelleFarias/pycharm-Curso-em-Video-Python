#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.


qtde = input('Quantos números deseja inserir? ')
while not qtde.isdigit():
    print('Valor inválido.')
    qtde = input('Quantos números deseja inserir? ')
qtde = int(qtde)
print('\nOk! Vamos começar!')

conjunto = []
soma = 0
for n in range(1, qtde+1):
    num = input(f'Digite o {n} número (entre 0 e 1000) → ')

    while not (num.isdigit() and 0 <= int(num) <= 1000):
        print('Valor inválido.')
        num = input(f'Digite o {n} número → ')
    num = int(num)
    conjunto.append(num)
    soma += num

print(f'\nO conjunto formado foi: {conjunto}')
print(f'O maior número é {max(conjunto)}.')
print(f'O menor número é {min(conjunto)}.')
print(f'A soma de todos os números é {soma}.')
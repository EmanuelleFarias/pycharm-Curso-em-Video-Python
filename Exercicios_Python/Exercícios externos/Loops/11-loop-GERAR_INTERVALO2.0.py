#Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Digite um número: '))
num2 = int(input('Agora digite um número maior: '))

soma = 0
for n in range(num1 + 1,num2):
    print(n, end=' ')
    soma += n
print(f'\nA soma dos números é {soma}.')
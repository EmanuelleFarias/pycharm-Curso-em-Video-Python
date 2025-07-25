#Faça um programa que leia 5 números e informe o maior número.


num = []
for n in range(1,6):
    numero = int(input('Informe um número: '))
    num.append(numero)
print(f'O maior número digitado foi {max(num)}')
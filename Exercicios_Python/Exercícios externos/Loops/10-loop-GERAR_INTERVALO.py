#Faça um programa que receba dois números inteiros e gere os números inteiros que
# estão no intervalo compreendido por eles.

num1 = int(input('Digite um número: '))
num2 = int(input('Agora digite um número maior: '))

for n in range(num1 + 1,num2):
    print(n, end=' ')
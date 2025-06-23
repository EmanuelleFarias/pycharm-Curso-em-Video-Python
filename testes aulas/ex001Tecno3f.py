#Realizar un programa que me diga si un número es par o impar

print(
    '========== PAR OU IMPAR =========='
)
num = int(input('Digite um número inteiro: '))
print()
if num % 2 == 0:
    print('{} é um número par'.format(num))
else:
    print('{} é um número ímpar.'.format(num))
'''Encontrar números primos é uma tarefa difícil. Faça um programa que gera
uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.'''

print('...'*20)
print(f"{' 🔢 Lista de Primos 🔢':^60}")
print('...'*20)
print('')


num = int(input('Quero a lista de números primos no intervalo entre 1 e → '))

lista = []
nao = []
cont = 0
for n in range(2, num + 1):
    primo = True
    for i in range(2, n):
        cont += 1
        if n % i == 0:
            primo = False
            nao.append(n)
            break
    if primo:
        lista.append(n)
print(f'\nLista dos números primos entre 1 e {num}: \n')
print((', '.join(str(primo) for primo in lista)))
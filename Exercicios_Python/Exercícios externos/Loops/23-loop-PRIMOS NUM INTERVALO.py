

'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
fornecido pelo usuário. O programa deverá mostrar também o número de divisões que
ele executou para encontrar os números primos. Serão avaliados o funcionamento, o
estilo e o número de testes (divisões) executados.'''

print('...'*20)
print(f"{'programa de numeros primos':^60}")
print('...'*20)

num = int(input('Qual o tamanho do intervalo você deseja? De 1 a → '))

primos = []
nao_primos = []
cont = 0
for n in range(2,num + 1):
    e_primo = True
    for i in range(2, n):
        cont += 1
        if n % i == 0:
            e_primo = False
            nao_primos.append(n)
            break
    if e_primo:
        primos.append(n)
print(f"Foram realizadas {cont} divisões.")
print(primos)



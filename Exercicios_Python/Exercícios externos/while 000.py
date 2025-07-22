VIDEO DO YOUTUBE TORQUATO (TÁ SALVO NO TELEGRAM)
#exemplo 1
a = 1
while (a <= 5):
    print('Número: ', a)
    a += 1
print()
#emeplo 2 (é a mesma coisa do ex anterior só que feito de uma forma diferente)

valor = 1 #começa em 1
limite = 5 # vai até 5

while valor <= limite:
    print('Número: ', valor)
    valor += 1 # sempre incrementa com 1 pq senão o contador (a varíavel) fica estática em 0 infinitamente
print()
#exemplo 3

print('Somar números. 0 para sair.')

número_input = 1
somatória = 0

while número_input != 0: #enquanto o numero de input for diferente de zero
    número_input = int(input('Digite um número: '))
    if número_input == 0:
        break
    somatória += número_input
print('A soma total dos números digitados é ', somatória)
print()
#exemplo 4 - soma com limite
total = 0
número = int(input('Digite um número para somar: '))

while (total <= 100):
    número = int(input('Digite um número para somar: '))
    total += número

print('O total excedeu 100. A soma de todos os números digitados é', total)




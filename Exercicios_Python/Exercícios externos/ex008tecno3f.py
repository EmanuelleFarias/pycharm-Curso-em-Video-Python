#Realizar un programa que pida al usuario que ingrese varios números y
# que devuelva la suma del cuadrado de esos números

#num = int(input('Digite um número (para finalizar digite 0): '))

soma = 0
cont = 0
while True:
    num = int(input('Digite um número (para finalizar digite 0): '))
    cont += 1
    quad = num * num
    soma += quad
    if num == 0:
        print(f'A soma do quadrado dos valores é {soma}.')
        break


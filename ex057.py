'''Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.'''
sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
while sexo not in 'MF':
    print('Por favor, escolha entre M ou F.\n')
    sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
    continue
print('Sexo escolhido: {}'.format(sexo))




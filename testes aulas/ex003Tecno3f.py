#Realizar un programa que le pida al usuario su nombre y edad y nos diga si es mayor de edad
#
nome = input('Digiter seu nome: ')
idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Oi, {}!!! Você tem {} anos. Logo, vc é menor de idade.'.format(nome, idade))
else:
    print('Oi, {}!!! Você tem {} anos. Logo, vc é maior de idade.'.format(nome, idade))
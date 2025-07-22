#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
#pedindo até que o usuário informe um valor válido.

nota = float(input('digite uma nota entre 1 e 10: '))

if nota < 1 or nota > 10:
    print('\033[7;30;43mValor inválido!!!\033[m')
    print('\033[1;0;43mDigite uma nota entre 1 e 10.\033[m')
else:
    print(nota)
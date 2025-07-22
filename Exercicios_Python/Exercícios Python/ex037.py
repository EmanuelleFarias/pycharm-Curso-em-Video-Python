num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido em BINÁRIO é {}.'.format(num, bin(num)))
elif op == 2:
    print(' {} convertido em OCTAL é {}.'.format(num, oct(num)))
elif op == 3:
    print('{} convertido em HEXADECIMAL é {}.'.format(num, hex(num)))
else:
    print('Esta opção não existe. Escolha entre 1, 2 ou 3.')

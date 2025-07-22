from time import sleep
n = int(input('digite um número: '))
print('')
print('deixa eu ver aqui...')
sleep(2)
if n % 2 == 0:
    print('>>> O número {} é par! <<<'.format(n))
else:
    print('O número {} é ímpar!'.format(n))

#outro jeito
r = n % 2
if r == 0:
    print('>>> O número {} é par! <<<'.format(n))
else:
    print('O número {} é ímpar!'.format(n))




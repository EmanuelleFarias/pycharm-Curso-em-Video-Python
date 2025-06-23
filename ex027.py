n = str(input('digite seu nome completo: ')).strip().split()
n1 = n[0]
nu = n[-1]
print(' o primeiro nome é {}.'.format(n1))
print(' o último nome é {}.'.format(nu))

#outro jeito

print('o último nome é {}.'.format(n[len(n)-1])) #len de nome mostra quantas posições tem o nome que já tá dividido em listas
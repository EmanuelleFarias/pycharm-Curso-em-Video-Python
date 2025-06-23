f = str(input('digite uma frase: ')).strip().lower()
l = len(f)
a = f.count('a')
f1 = f.find('a')
f2 = f.rfind('a')
print(l)
print('A letra A aparece {} vezes na frase.'.format(a))
print('A primeira ocorrência da letra A foi em {}'.format(f1+1)) #bota o +1 pra poder adequar ao usuário, pq no python começa a contagem no 0 e pra nós começa no 1
print('A última ocorrência da letra A foi em {}'.format(f2+1))
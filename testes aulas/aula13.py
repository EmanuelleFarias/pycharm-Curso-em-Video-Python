for c in range(1,7): # ele sempre ignora o último número da contagem
    #print(c)
print('fim') # se eu identar o print com 1 tab ele vai incluir no comando principal>>>como no próximo exemplo

for c in range (1,5):
    #print(c)
    #print('pronto')

#>>>contagem regressiva
for c in range (10,0,-1): #coloca o -1 no final
    print (c)

#>>>contagem com intervalos
for c in range (0,10,3): # o último número é o que corresponde ao intervalo
    print(c)

#>>>contagem com input
n = int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print('fim')

#>>>intervalo com input
i = int(input('Início: ')) #começa a contagem com esse número diggitado ex: 2
f = int(input('Fim: ')) #termina nesse número digitado ex: 9
p = int(input('Passo: ')) # p de passo = tipo uma progressão ex: 3
for c in range(i, f+1, p):
    print(c) #a resposta será 2, 5, 8 (pq 2+3+5, 5+3+8)
print('fim')

#>>>repetição de input
for c in range(0, 3):
    n = int(input('Digite um valor: ')) # vai pedir essa informação 3x
print('fim')
#>>>resposta:
#Digite um valor: 2
#Digite um valor: 1
#Digite um valor: 4
#fim
#com comando além do input
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n #pode escrever s+=n que o python aceita
print('A soma de tudo é {}.'.format(s))


S = 0
for x in range(1, 500):
    if x % 2 != 0 and x % 3 == 0:
        S = S + x
print(S)
#------  PRIMEIRA LISTA ------
from pygame.event import clear
from pygame.examples.music_drop_fade import music_file_list

dados = []
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('Joao')
dados.append(32)
print('dados')
print(dados)

print(dados[0])
print(dados[1])

#------ SEGUNDA LISTA ------

pessoas = []

pessoas.append(dados[:]) #lista dentro da lista ([:] = copia tudo)
print(pessoas)

print(pessoas[0][0])
print(pessoas[0][1])
print(pessoas[0][2])

pess = [['Pedro', 25], ['Maria', 19], ['Joao', 32]]
print(pess)

print(pess[0][0])
print(pess[0][1])
print(pess[1][1])
print(pess[1])


#------ TESTES ------

teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
galera.append(teste) #ligação entre as listas, não é cópia// galera.append(teste[:]) assim é copia
print(galera)

teste[0] = 'Maria'
teste[1] = 2
galera.append(teste) #ligação entre as listas, não é cópia// galera.append(teste[:]) assim é copia
print(galera)

galera = [['Ana', 28], ['Jorge', 30], ['Carlos', 45,], ['José', 50]]

print(galera)

for p in galera:
    print(f'{p[0]} tem {p[1]} anos.')

galera = list()
dados = list()
totmai = totmen = 0

for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear() #para limpar a lista dados, senao vai acumulando tudo

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')
print(galera)
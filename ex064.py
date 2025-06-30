'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

numero = int(input('Digite um número inteiro (tecle 999 para finalizar): '))
cont = 0
soma = 0
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número inteiro (tecle 999 para finalizar): ')) # a linha tem que ficar aqui no fim e não no começo do laço while pq A ORDEM IMPORTA. ele vai realizar os comandos em ordem dentro do laço.
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))



num, cont, sum=0,0,0 # == num=0 ↳ cont=0 ↳ sum=0
while num !=999:
  sum+=num
  cont+=1
  num = int(input('Digite un número entero ("999" para terminar): '))
print(cont-1, sum)
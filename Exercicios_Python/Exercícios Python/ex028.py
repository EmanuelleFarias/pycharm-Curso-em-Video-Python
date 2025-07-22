from random import randint
from time import sleep
import emoji
#faz o pc dizer um numero random inteiro
npc = randint(0,10)
print('')
print('Tente adivinhar em qual número estou pensando...')
print('~-~' *20)
nu = int(input('Vamos lá!!! Digite um número entre 0 e 10: '))
print('~.~'*20)
print('Que rufem os tambores...🥁')
sleep(2)
print('')
print('~~'*20)
if nu == npc: #se o número do usuário for igual ao número do computador
    print('Ora ora, temos um Sherock Romes aqui!!!🧐')
else: #se não
    print('Não foi dessa vez, meu caro Watson...🤷‍♂️')


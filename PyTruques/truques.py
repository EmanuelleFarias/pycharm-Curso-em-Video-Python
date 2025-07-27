#para pular linha
from html import unescape
>print('')

#pra não quebrar a linha escreve isso dentro da str
> ,end=''

#pra quebrar linha digita isso em qualquer lugar que queira quebrar
> \n

#pra saber o tipo primitivo de alguma coisa
> print(type(x))

#ordem de preferência dos operadores
> ()
>> **
>>> * / // %
>>>> + -

#concatenação
> usando +, une #com type int não dá certo
>> usando , (vírgula), fica um espaço

#módulos
> import math (e especifica a funcionalidade na str > math.trunc(x))
>> from math import trunc (só utiliza a funcionalidade sem precisar chamar o math novamente > trunc(x))

# grau pra copiar °

# digitar ''' desativa os comandos pra usar a tela pra testar outros comandos

# lista fica entre []

# entrada formatada
## escrevo um print
##ex: print(' Lojinha '). aí eu abro os {} dentro do print
### ex: print ('{}'.format(' Lojinha ')). aí eu escrevo dentro dos {} a formatação que quero.
### ex: print('{:=^40}'.format(' Lojinha ')) >>> o que tá dentro do parênteses, neste caso, é >:< isso >^< centralizado em >40< espaços

#print('-='*11) # -=-=-=-=-=-=-=-=-=-=-= (aba 45)

# print('O computador jogou {}.'.format(itens[opc]))# format = dentro da lista de itens, a posição [opc] (aba 45)

# pra tirar espaços no meio da frase
###f = f.strip().replace(' ','') #frase sem espaço

# sinal de ª para copiar
# sinal de ↓ ← ↑ → ↔ ↕ ↖ ↗ ↘ ↙ ↩ ↪ ↲ ↳para copiar

# coisas com listas no exercício 70

'''pra unir quando printo os itens de uma lista
-> print(', '.join(str(i) for i in seq)) /// usei na aba 15-loop'''

'''quando já é string -> 
print(', '.join (letras for letras in palavra if letras in 'aeiou'))//usei no Aex74 - exercicios externos'''
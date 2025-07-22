''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

i = 0
mv = 0
nmv = ''
si = 0
m20a = 0
li = []
for c in range(1,5):
    n = str(input('nome da {}ª pessoa: '.format(c))).strip()
    i = int(input('idade da {}ª pessoa: '.format(c)))
    s = str(input('sexo da {}ª pessoa: '.format(c))).strip()
    print('')
    si = si + i
    m = si / 4
    li += [i]
    if s == 'm' or s == 'M':
        if i > mv:
            mv = i
            nmv = n
    elif s == 'f' or s == 'F':
        if i < 20:
            m20a += 1

print('')
print('A média entre todas as idades é {}.'.format(m))
print('a maior idade é {}.'.format(max(li)))
print('O homem mais velho é {} e tem {} anos.'.format(nmv, mv))
print('Existem {} mulheres com menos de 20 anos.'.format(m20a))


#outro jeito (aula)

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and s in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))





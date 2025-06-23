nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana, Cláudia, Mariana , Juliana':
    print('Belo nome feminino!')
else: #se tirar o else ele apenas dá o bom dia, que é o último print
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

nome = str(input('digite seu nome completo')) #Joao da Silva
ma = nome.upper() # retorna Nome em maiúsculas: JOAO DA SILVA.
mi = nome.lower() # retorna Nome em minúsculas: joao da silva.
ql = len(nome)- nome.count(' ') # retorna A quantidade de letras é: 11.
ln = nome.split()
n1 = ln[0] # retorna Seu primeiro nome é: Joao.
#o [0] é onde tá o primeiro nome na lista.
ln1 = len(n1) # retorna Seu primeiro nome tem 4 letras.
print('Nome em maiúsculas: {}.\n' 'Nome em minúsculas: {}.\n' 'A quantidade de letras é: {}.\n' 'Seu primeiro nome é: {}.\n' 'Seu primeiro nome tem {} letras.' .format(ma,mi,ql,n1,ln1))


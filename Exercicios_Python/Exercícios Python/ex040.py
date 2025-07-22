pn = float(input('Primeira nota:'))
sn = float(input('Segunda nota:'))
m = (pn + sn)/2
print('Tirando {} e {}, a média do aluno é {}.'.format(pn, sn, m))
if m < 5:
    print('O aluno está \033[1;31mREPROVADO.')
elif m >= 5 and m < 7: # ou 7 > m >= 5
    print('O aluno está em \033[1;33mRECUPERAÇÃO.')
elif m >= 7:
    print('O aluno está \033[1;32mAPROVADO.')

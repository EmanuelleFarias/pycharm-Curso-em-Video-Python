from Tools.scripts.generate_global_objects import Printer

#Realizar un programa que pida al usuario su edad y nos diga si debe votar,y en caso de tener entre 16 y 18. preguntar
# l usuario si decide votar o no

print(
    '====== PROGRAMA DE VOTAÇÃO ======')
idade = int(input('Digite sua idade: '))
print()
if idade <16:
    print('Você tem {} anos. Ainda não chegou seu momento de votar!'.format(idade))
elif idade <18:
    print('Você tem {} anos. Nessa idade o voto não é obrigatório. Mas você pode votar se quiser!!!'.format(idade))
    print()
    pergunta = input('Você deseja votar este ano?[SIM/NAO]').strip().lower()
    while pergunta not in'simnao':
        print('\033[1;31mResposta inválida!!!\033[m Digite SIM ou NAO.')
        print()
        pergunta = input('Você deseja votar este ano?[SIM/NAO]').strip().lower()
        print()
        if pergunta == 'sim':
            print('Parabéns pela escolha de exercer sua cidadania por meio do voto!!!')

        if pergunta == 'nao':
            print('Tudo bem...Talvez na próxima eleição possamos contar com seu voto.')
    if pergunta == 'sim':
        print('Parabéns pela escolha de exercer sua cidadania por meio do voto!!!')

    if pergunta == 'nao':
        print('Tudo bem...Talvez na próxima eleição possamos contar com seu voto.')
else:
    print('Não tem como escapar, você tem que votar!!!')
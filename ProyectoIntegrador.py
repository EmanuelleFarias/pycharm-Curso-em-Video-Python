'''Se ha pedido crear un modulo para generar ticktes que contenga lo siguiente:

Un menu con 3 opciones - Alta ticket , Leer ticket , Salir.

Alta ticket : nombre, sector,asunto, problemaAl terminar de ingresar
el ticket se debera mostrar por pantalla el mismo,sumandose el numero
de ticket (que sera un numero random entre 1000,9999) y una leyenda que
pida acordarse del numeroun menu que nos pregunte si deseamos crear otro
ticket, en caso de ser noque nos regrese al menu principal, de lo contrario
que nos regrese a lapantalla de alta.

leer ticet: numero ticketal ingresar el
numero nos mostrara por pantalla el ticket almacenadodebajo del mismo aparece
una leyanda que nos preguntara si deseamos leerotro ticket, teniendo la funcionalidad
similar a la anteriormente mensionada.

Salir : el programa finaliza y se cierra pidiendonos una confirmacion'''
from random import randint

while True:
    print('==' * 30)
    print('{:^60}'.format('¡Hola! Bienvenido al Sistema de Tickets'))
    print('==' * 30)
    print(''' Seleccione una opción:

[1] Generar un nuevo ticket
[2] Leer un ticket
[3] Salir 
    ''')

    opcion = int(input('Opción seleccionada: '))
    if opcion == 1:
        while True:
            print('\nIngrese los datos para generar un nuevo ticket')
            nombre = str(input('Ingrese su Nombre: '))
            sector = str(input('Ingrese su Sector: '))
            asunto = str(input('Ingrese Asunto: '))
            mensaje = str(input('Ingrese un Mensaje: '))

            print('=='*30)
            print('{:^60}'.format('Se generó el siguiente Ticket'))
            print('=='*30)
            print(f'''    
    Su Nombre: {nombre}          N Ticket: {randint(1000,9999)}
    Sector: {sector}
    Asunto: {asunto}
    
    Mensaje: {mensaje}    
           ''')
            print('{:^60}'.format('Recordar su número de Ticket'))

            nuevo = str(input('\nDesea generar un nuevo Ticket?(S/N) ')).strip().lower()
            while nuevo not in 'sn':
                print('Ingrese S para Sí o N para No')
                nuevo = str(input('\nDesea generar un nuevo Ticket?(S/N) ')).strip().lower()
            if nuevo == 'n':
                print()
                break




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
tickets = {}

#def limpiar_pantalla():
    #os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_ticket(ticket):
    print()
    print('{:^60}'.format('TICKET'))
    print(f'╔{"═" * 58}╗')
    print(f'''    
    Su Nombre: {ticket['nombre']}          Nº Ticket: {ticket['numero']}
    Sector: {ticket['sector']}
   #Asunto: {ticket['asunto']}

    Mensaje: {ticket['mensaje']}
      # ''')
    print(f'╚{"═" * 58}╝')


def alta_ticket():
    while True:
        #limpiar_pantalla()
        print('—'*60)
        print('Ingrese los datos para generar un nuevo ticket')
        print('—'*60)
        nombre = str(input('Ingrese su Nombre: '))
        sector = str(input('Ingrese su Sector: '))
        asunto = str(input('Ingrese Asunto: '))
        mensaje = str(input('Ingrese un Mensaje: '))
        numero = randint(1000, 9999)
        print('--' * 30)
        print('{:^60}'.format('Se generó el siguiente Ticket'))
        print('--' * 30)
        ticket = {
                'numero': numero,
                'nombre': nombre,
                'sector': sector,
                'asunto': asunto,
                'mensaje': mensaje
                 }
        tickets[numero] = ticket
        mostrar_ticket(ticket)
        print('{:^60}'.format('🎫 Recordar su número de Ticket ✏️'))

        nuevo = str(input('\n⫸¿Desea generar un nuevo Ticket?(S/N) ')).strip().lower()
        while nuevo not in 'sn':
            print('Ingrese S para Sí o N para No')
            nuevo = str(input('\n⫸¿Desea generar un nuevo Ticket?(S/N) ')).strip().lower()
        if nuevo == 'n':
            print()
            break


def leer_ticket():
    while True:
        #limpiar_pantalla()
        print('—' * 60)
        print('{:^60}'.format('🎫 Lectura de Ticket'))
        print('—' * 60)
        try:
            numero = int(input('Ingrese el número de ticket: '))
            if numero in tickets:
                mostrar_ticket(tickets[numero])
            else:
                print('\n❌ Ticket no encontrado.')
        except ValueError:
            print('\n⚠️ Ingrese un número válido.')

        nuevo = input('\n⫸¿Desea leer otro ticket? (S/N): ').strip().lower()
        while nuevo not in 'sn':
            nuevo = input('Ingrese S para sí o N para no: ').strip().lower()
        if nuevo == 'n':
            break

def salir():
    confirmacion = input('\n⫸¿Está seguro que desea salir? (S/N): ').strip().lower()
    while confirmacion not in ('s', 'n'):
        confirmacion = input('Ingrese S para Sí o N para No: ').strip().lower()
    return confirmacion == 's'


while True:
    #limpiar_pantalla()
    print('==' * 30)
    print('{:^60}'.format(' 🎫¡Hola! Bienvenido al Sistema de Tickets 🎫' ))
    print('==' * 30)
    print(''' Seleccione una opción:

[1] Generar un nuevo ticket
[2] Leer un ticket
[3] Salir 
    ''')

    opcion = int(input('Opción seleccionada: '))
    if opcion == 1:
        alta_ticket()
    elif opcion == 2:
        leer_ticket()
    else:
        salir()
        print('—' * 60)
        print('{:^60}'.format('🔴 Programa Finalizado. ¡Hasta luego!'))
        print('—' * 60)
        print()



from random import randint
import os
import json
import sys

archivo = 'tickets.json'
tickets = {}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_tickets():
    global tickets
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            tickets = json.load(f)
    else:
        tickets = {}

def salvar_tickets(tickets_dict):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(tickets_dict, f, indent=4, ensure_ascii=False)

def mostrar_ticket(ticket):
    print()
    print('{:^60}'.format('TICKET'))
    print(f'╔{"═" * 58}╗')
    print(f'''
    Su Nombre: {ticket['nombre']}          Nº Ticket: {ticket['numero']}
    Sector: {ticket['sector']}
    Asunto: {ticket['asunto']}

    Mensaje: {ticket['mensaje']}
       ''')
    print(f'╚{"═" * 58}╝')

def alta_ticket():
    while True:
        limpiar_pantalla()
        print('—' * 60)
        print('{:^60}'.format('Ingrese los datos para generar un nuevo ticket'))
        print('—' * 60)
        nombre = input('Ingrese su Nombre: ')
        sector = input('Ingrese su Sector: ')
        asunto = input('Ingrese Asunto: ')
        mensaje = input('Ingrese un Mensaje: ')
        numero = str(randint(1000, 9999))

        ticket = {
            'numero': numero,
            'nombre': nombre,
            'sector': sector,
            'asunto': asunto,
            'mensaje': mensaje
        }

        tickets[numero] = ticket
        salvar_tickets(tickets)
        limpiar_pantalla()
        print('--' * 30)
        print('{:^60}'.format('Se generó el siguiente Ticket'))
        print('--' * 30)
        mostrar_ticket(ticket)
        print('{:^60}'.format('🎫 Recordar su número de Ticket ✏️'))

        nuevo = input('\n⫸¿Desea generar un nuevo Ticket? (S/N): ').strip().lower()
        while nuevo not in 'sn':
            print('Ingrese S para Sí o N para No')
            nuevo = input('\n⫸¿Desea generar un nuevo Ticket? (S/N): ').strip().lower()
        if nuevo == 'n':
            break

def leer_ticket():
    while True:
        limpiar_pantalla()
        print('—' * 60)
        print('{:^60}'.format('🎫 Lectura de Ticket'))
        print('—' * 60)
        numero = input('Ingrese el número de ticket: ').strip()
        ticket = tickets.get(numero)
        if ticket:
            mostrar_ticket(ticket)
        else:
            print('\n❌ Ticket no encontrado.')

        nuevo = input('\n⫸¿Desea leer otro ticket? (S/N): ').strip().lower()
        while nuevo not in 'sn':
            nuevo = input('Ingrese S para Sí o N para No: ').strip().lower()
        if nuevo == 'n':
            break

def salir():
    confirmacion = input('\n⫸¿Está seguro que desea salir? (S/N): ').strip().lower()
    while confirmacion not in ('s', 'n'):
        confirmacion = input('Ingrese S para Sí o N para No: ').strip().lower()
    if confirmacion == 's':
        print('—' * 60)
        print('{:^60}'.format('🔴 Programa Finalizado. ¡Hasta luego!'))
        print('—' * 60)
        sys.exit()

def menu_principal():
    cargar_tickets()
    while True:
        limpiar_pantalla()
        print('==' * 30)
        print('{:^60}'.format('🎫 ¡Hola! Bienvenido al Sistema de Tickets 🎫'))
        print('==' * 30)
        print('''Seleccione una opción:

[1] Generar un nuevo ticket
[2] Leer un ticket
[3] Salir
        ''')
        try:
            opcion = int(input('Opción seleccionada: '))
        except ValueError:
            print('\n⚠️ Ingrese una opción válida.')
            input('Presione Enter para continuar...')
            continue

        if opcion == 1:
            alta_ticket()
        elif opcion == 2:
            leer_ticket()
        elif opcion == 3:
            salir()
        else:
            print('\n⚠️ Opción no válida.')
            input('Presione Enter para continuar...')

if __name__ == "__main__":
    menu_principal()
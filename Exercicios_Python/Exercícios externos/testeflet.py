#def mostrar_tablero_amplio(tablero):
print()
print(("+" + "-----")*3 + "+")
for fila in tablero:
    print(("|" + "     ")*3 + "|")
    print("|  {}  |  {}  |  {}  |".format(*fila))
    print(("|" + "     ")*3 + "|")
    print(("+" + "-----")*3 + "+")
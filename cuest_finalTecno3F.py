'''numero = 33

if numero > 22:
    print("El numero es Mayor")
if numero == 22:
    print("El numero es Igual")
else:
    print("El numero es Menor")'''

'''while True:
    palabra = input("ingrese una palabra de mas de 5 letras: ")

    if len(palabra) > 5:
        print("Su palabra tiene mas de 5 letras")
        return palabra
    else:
        print("Palabra demasiado corta, ingrese otra")'''

'''def palabra():
    while True:
        palabra = input("ingrese una palabra de mas de 5 letras: ")

        if len(palabra) > 5:
            print("Su palabra tiene mas de 5 letras")
            return palabra
        else:
            print("Palabra demasiado corta, ingrese otra")

palavra_digitada = palabra()
print(f"A palavra aceita foi: {palavra_digitada}")'''
'''#mifuncion(4)
def mifuncion():
    x = 4
    x += 3
    x = x-1
    print(x)
mifuncion()
#print(x)

 # Esto imprimiría 6'''

'''def mifuncion(y):
    x = 4 + y
    y += 3
    x = (y-1) * x
    print(x)

mifuncion(5)'''

x = 3
y = 3+4
z = 0

z = y
x = (z + y) - x
y = x + z
z = z + x
z = x
x = y - z
y = z
x = (x + x) - 3

print(x,y,z)

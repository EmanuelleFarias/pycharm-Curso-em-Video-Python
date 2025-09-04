A = {'azul', 'amarillo', 'naranja', 'blanco', 'amarillo'}
B = {'rosa', 'rojo', 'azul'}





print('---'*20)
#1

print(A)
print(B)
print(A|B)

def imprimir_union(A, B):
    union = A | B
    print("Elementos en A o B (o ambos):")
    for elemento in union:
        print(elemento)

if __name__ == "__main__":
    A = {'azul', 'amarillo', 'naranja', 'blanco', 'amarillo'}
    B = {'rosa', 'rojo', 'azul'}
    imprimir_union(A, B)


print('---'*20)
#2

print(A&B)

def imprimir_interseccion(A, B):
        interseccion = A & B
        print('Elementos que están en A y B:')
        for elemento in interseccion:
            print(elemento)


if __name__ == "__main__":
    A = {'azul', 'amarillo', 'naranja', 'blanco', 'amarillo'}
    B = {'rosa', 'rojo', 'azul'}
    imprimir_interseccion(A, B)

print('---'*20)
#3

print(A-B)

def imprimir_soloA(A, B):
    soloA = A - B
    print('Elementos que están apenas en el conjunto A:')
    for elemento in soloA:
        print(elemento)


if __name__ == "__main__":
    A = {'azul', 'amarillo', 'naranja', 'blanco', 'amarillo'}
    B = {'rosa', 'rojo', 'azul'}
    imprimir_soloA(A, B)

print(B-A)

def imprimir_soloB(A, B):
    soloB = B - A
    print('Elementos que están apenas en el conjunto B:')
    for elemento in soloB:
        print(elemento)


if __name__ == "__main__":
    A = {'azul', 'amarillo', 'naranja', 'blanco', 'amarillo'}
    B = {'rosa', 'rojo', 'azul'}
    imprimir_soloB(A, B)

print('---'*20)
#4

print(A.issubset(B))

def subconjunto(A, B):
    subconjunto = A.issubset(B)
    if A.issubset(B):
        print('A es un subconjunto de B.')
    else:
        print('A no es un subconjunto de B.')


if __name__ == "__main__":
    A = {'azul', 'amarillo', 'naranja', 'blanco', 'amarillo'}
    B = {'rosa', 'rojo', 'azul'}
    subconjunto(A, B)

print('---'*20)
#5

print(len(A))

def contar_elementos(A):
    cantidad = len(A)
    print(f'El conjunto A tiene {cantidad} elementos.')

if __name__ == "__main__":
    A = {'azul', 'amarillo', 'naranja', 'blanco', 'amarillo'}
    B = {'rosa', 'rojo', 'azul'}
    contar_elementos(A)

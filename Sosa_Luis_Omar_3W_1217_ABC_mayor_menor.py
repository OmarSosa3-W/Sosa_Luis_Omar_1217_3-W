print(" ")#se coloca para poner un espacio
print("Sosa Luis Omar 3-W: Mi practica de examen de numero mayor")#nombre del creador del codigo
print(" ")#se coloca para poner un espacio
A = float(input("Ingrese el primer valor: "))#pide al usuario que ingrese un valor
B = float(input("Ingrese el segundo valor: "))#pide al usuario que ingrese un valor
C = float(input("Ingrese el tercer valor: "))#pide al usuario que ingrese un valor

# Comprobar si los valores son distintos
if A == B or A == C or B == C:#se diferencian los valores de las variables
    print("Los valores deben ser distintos.")#muestra en pantalla que los valores no se deben repetir
else:#opcion de que pasa si no se cumple la funcion
    # Encontrar el mayor y el menor
    mayor = A#el valor del numero mayor 
    menor = A#el valor del numero menor
    print(" ")#se coloca para poner un espacio

    if B > mayor:#el valor del numero mayor 
        mayor = B#el valor del numero mayor 
        print(" ")#se coloca para poner un espacio
    if C > mayor:#el valor del numero mayor 
        mayor = C#el valor del numero mayor 
    if B < menor:#el valor del numero menor
        print(" ")#se coloca para poner un espacio
        menor = B#el valor del numero menor
    if C < menor:#el valor del numero menor
        print(" ")#se coloca para poner un espacio
        menor = C#el valor del numero menor

    print("El mayor es:", mayor)#mustra en pantalla el resultado 
    print("El menor es:", menor)#mustra en pantalla el resultado 
    print(" ")#se coloca para poner un espacio80
import math

pi = 3.1416

b = float(input("Ingrese el lado b del triangulo: "))
c = float(input("Ingrese el lado c del triangulo: "))
alpha = float(input("Ingrese el angulo que hay entre los dos lados (expresado en grados sexagesimales): "))

a = (b**2 + c**2 - 2*b*c * math.cos(alpha*pi/180))**0.50

print("El lado a vale: ", a)

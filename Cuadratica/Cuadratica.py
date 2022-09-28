import cmath
import math


def cuadratica(a, b, c):
    if ((b*b) - (4*a*c)) > 0:
        x1 = (-b + (math.sqrt((b*b) - (4*a*c)))) / (2*a)
        x2 = (-b - (math.sqrt((b*b) - (4*a*c)))) / (2*a)
        print("El valor de x1 ="+str(x1))
        print("El valor de x2 ="+str(x2))


def cuadraticaImaginaria(a, b, c):
    if ((b*b) - (4*a*c)) < 0:
        x1 = (-b + (cmath.sqrt((b*b) - (4*a*c)))) / (2*a)
        x2 = (-b - (cmath.sqrt((b*b) - (4*a*c)))) / (2*a)
        print("Solucion compleja")
        print("El valor de x1 ="+str(x1))
        print("El valor de x2 ="+str(x2))

        print("x1 = ", x1.real, "x", x1.imag, "i")
        print("x2 = ", x2.real, "x", x2.imag, "i")


cuadratica(2, 4, 2)
cuadraticaImaginaria(18, -36, 7)

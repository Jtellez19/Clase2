import math


class Calculadora:
    def suma(self, a, b):
        suma = a+b
        print("Suma: ", suma)

    def resta(self, a, b):
        resta = a-b
        print("Resta:", resta)

    def multiplicacion(self, a, b):
        multi = a*b
        print("Multiplicacion:", multi)

    def division(self, a, b):
        if b == 0:
            print("No se puede dividir entre cero")
        else:
            division = a/b
            print("Division:", division)

    def raiz(self, a):
        r = 0
        if a < 0:
            print("La raiz de este numero genera numeros complejos")
        else:
            r = math.sqrt(a)
        print("Raiz cuadrada:", r)

    def exponencial(self, a, b):
        exp = a**b
        print("Exponencial:", exp)


calc = Calculadora()
calc.suma(1, 2)
calc.resta(4, 2)
calc.multiplicacion(2, 2)
calc.division(2, 2)
calc.raiz(4)
calc.exponencial(5, 2)

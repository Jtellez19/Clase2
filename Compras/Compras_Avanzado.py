tiempo = -1
acumulado = 0
horas = 0
horas_aux = 0
total = 0

while tiempo != 0:
    tiempo = int(input("Minutos a capturar: "))
    if tiempo > 0:
        acumulado += tiempo
    elif tiempo < 0:
        print("Ingresa valores positivos")

horas = acumulado/60
if horas >= 8:
    total = 200
elif horas <= 1:
    total = 25
elif horas > 1:
    horas_aux = int(horas)
    if horas_aux > 0:
        total = (horas-1)*15 + 25
    else:
        total = 40


print("La cantidad a pagar es de: $"+str(total))

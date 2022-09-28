compras = -1
acumulado = 0

while compras != 0:
    compras = int(input("Monto de compra: "))
    if compras > 0:
        acumulado += compras
    elif compras < 0:
        print("Ingresa valores positivos")
if acumulado >= 1000:
    acumulado = acumulado-(acumulado*0.10)
    print("Ha obtenido un descuento del 10%")
print("La cantidad a pagar es de: "+str(acumulado))

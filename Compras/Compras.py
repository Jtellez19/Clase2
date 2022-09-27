compras = -1
acumulado = 0

while compras != 0:
    compras = int(input("Monto de compra: "))
    if compras > 0:
        acumulado += compras
    elif compras < 0:
        print("Ingresa valores positivos")

print("La cantidad a pagar es de: "+str(acumulado))

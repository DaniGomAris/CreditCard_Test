import Payment

print("Este programa permite calcular la cuota a pagar por una compra con tarjeta de credito")
monto = float(input("Monto de la compra: "))
tasa = float(input("Interes de la tarjeta: "))
cuotas = float(input("Numero de cuotas en que va a inferir la compra: "))

print((Payment.CalculateFee(monto,tasa,cuotas)))

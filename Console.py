import Payment
import Amortizacion
import ExtraBonus

print("¡Bienvenido!, qué tipo de cálculo desea hacer?")

print("1. Compra con tarjeta de crédito y calcular el interes total")
print("2. Amortización")
print("3. Amortización con abono extra")
eleccion = int(input("\n\nEscriba el número de su elección: "))

if eleccion == 1:
    monto = float(input("Monto a pagar: "))
    tasa = float(input("Tasa actual: "))
    cuotas = int(input("Cúantas cuotas pagará el monto: "))
    print(Payment.monthly_bills(monto,tasa,cuotas))
if eleccion == 2:
    monto = float(input("Monto a pagar: "))
    tasa = float(input("Tasa actual: "))
    cuotas = int(input("Cúantas cuotas pagará el monto: "))
    print(Amortizacion.amortizacion(monto,tasa,cuotas))
if eleccion == 3:
    monto = float(input("Monto a pagar: "))
    tasa = float(input("Tasa actual: "))
    cuotas = int(input("Cúantas cuotas pagará el monto: "))
    numero_cuota_a_abonar = int(input("Qué cuota va a hacer un abono extra: "))
    abonoextra = float(input("Cúanto será el abono extra: "))
    print(ExtraBonus.amortizacion_extra_bonus(monto,tasa,cuotas,numero_cuota_a_abonar,abonoextra))

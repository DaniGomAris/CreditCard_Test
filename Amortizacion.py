import Payment

def Total_Interest(monto,tasa,cuotas):
    valor_cuota = Payment.CalculateFee(monto, tasa, cuotas)
    total_intereses = (valor_cuota * cuotas) - monto
    return total_intereses

def Amortizacion(monto, tasa, cuotas):
    valor_cuota = Payment.CalculateFee(monto, tasa, cuotas)
    print(valor_cuota)
    interes_x = tasa/100
    saldo = monto
    tabla_amortizacion = [["Cuota", "Saldo", "Pago interés", "Abono capital"], ["#", valor_cuota, tasa, monto]]
    if cuotas == 1:
        numero_cuota = 1
        interes = (tasa * saldo) / 100
        abono_capital = valor_cuota - interes
        fila = [numero_cuota, saldo, interes, abono_capital]
        tabla_amortizacion.append(fila)
    else:
        for cuota in range(1, cuotas + 1):
            numero_cuota = cuota
            interes = interes_x * saldo
            abono_capital = valor_cuota - interes
            saldo = saldo - abono_capital
            
            fila = [numero_cuota, saldo, interes, abono_capital]
            tabla_amortizacion.append(fila)
            print(fila)

    return tabla_amortizacion

monto = 850000
cuotas = 24
tasa_interes = 3.4

print(Amortizacion(monto, tasa_interes, cuotas))

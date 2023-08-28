import Payment
import Exceptions

def interes_total(monto,tasa,cuotas):
    valor_cuota = Payment.calculateFee(monto, tasa, cuotas)
    total_intereses = (valor_cuota * cuotas) - monto
    return total_intereses

def amortizacion_extra_bonus(monto, tasa, cuotas,numero_cuota_a_abonar,abonoextra):
    valor_cuota = Payment.calculateFee(monto, tasa, cuotas)
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
            if saldo <=0:
                break

            numero_cuota = cuota
            interes = interes_x * saldo

            if numero_cuota_a_abonar == numero_cuota:
                cuota_real_a_abonar = abonoextra
            else:
                cuota_real_a_abonar = valor_cuota
        
            abono_capital = cuota_real_a_abonar - interes
            saldo -= abono_capital
            
            if abonoextra < cuota_real_a_abonar:
                raise Exceptions.LowBonus
            
            if abonoextra > saldo:
                raise Exceptions.HighBonus

            if saldo < 0:
                abono_capital += saldo + interes
                saldo = 0

            fila = [numero_cuota, saldo, interes, abono_capital]
            tabla_amortizacion.append(fila)

        if saldo < abono_capital:
                abono_capital = saldo

    return tabla_amortizacion
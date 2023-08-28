import Payment
import Amortizacion
import ExtraBonus
import sys
from abc import ABC

class MenuConsole(ABC):
    def menu_option(self):
        print("""
Menu
1. Compra con tarjeta de crédito y calcular el interes total")
2. Amortizacion
3. Amortizacion con abono extra
4. Salir
                    """)
    
    def election_option(self):
        self.menu_option()
        eleccion = int(input("Opcion: "))

        if eleccion == 1:
            self.calculateFee_option()

        if eleccion == 2:
            self.amortizacion_option()

        if eleccion == 3:
            self.extra_bonus_option()

        if eleccion == 4:
            sys.exit()

    def calculateFee_option(self):
        monto = float(input("Monto a pagar: "))
        tasa = float(input("Tasa actual: "))
        cuotas = int(input("Cúantas cuotas pagará el monto: "))
        print(f"Total interests: {Payment.calculateFee(monto,tasa,cuotas)}")
        self.election_option()
        
    def amortizacion_option(self):
        monto = float(input("Monto a pagar: "))
        tasa = float(input("Tasa actual: "))
        cuotas = int(input("Cúantas cuotas pagará el monto: "))
        print(Amortizacion.amortizacion(monto,tasa,cuotas))
        self.election_option()
        
    def extra_bonus_option(self):
        monto = float(input("Monto a pagar: "))
        tasa = float(input("Tasa actual: "))
        cuotas = int(input("Cúantas cuotas pagará el monto: "))
        numero_cuota_a_abonar = int(input("Qué cuota va a hacer un abono extra: "))
        abonoextra = float(input("Cúanto será el abono extra: "))
        print(ExtraBonus.amortizacion_extra_bonus(monto,tasa,cuotas,numero_cuota_a_abonar,abonoextra))
        self.election_option()
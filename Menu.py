from Payment import Payment
from Amortization import Amortization
from ExtraBonus import ExtraBonus
import sys

class MenuConsole:
    
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
        amount = float(input("Monto a pagar: "))
        rate = float(input("Tasa actual: "))
        pay = int(input("Cúantas cuotas pagará el monto: "))
        print(f"Total interests: {Payment.CreditCardPayment.calculateFee(amount, rate, pay)}")
        self.election_option()
        

    def amortizacion_option(self):
        amount = float(input("Monto a pagar: "))
        rate = float(input("Tasa actual: "))
        pay = int(input("Cúantas cuotas pagará el monto: "))
        print(Amortization.CreditCardAmortizacion.amortizacion(amount, rate, pay))
        self.election_option()
   
        
    def extra_bonus_option(self):
        amount = float(input("Monto a pagar: "))
        rate = float(input("Tasa actual: "))
        pay = int(input("Cúantas cuotas pagará el monto: "))
        number_pay_of_bonus = int(input("Qué cuota va a hacer un abono extra: "))
        extrabonus = float(input("Cúanto será el abono extra: "))
        print(ExtraBonus.CreditCardExtraBonus.extra_bonus(amount, rate, pay, number_pay_of_bonus, extrabonus ))
        self.election_option()

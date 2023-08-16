import unittest
import Payment
import Amortizacion

class CreditCardTest(unittest.TestCase):

    def Normal_Case(self):
        monto = 200000
        tasa = 3.1
        cuotas = 36
        cuota = 9297.96
        resultado = Payment.CalculateFee( monto, tasa, cuotas)

        self.assertEqual(cuota, round(resultado,2))

    def Normal_Case2(self):
        monto = 850000
        tasa = 3.4
        cuotas = 24
        cuota = 52377.5
        resultado = Payment.CalculateFee(monto, tasa, cuotas)

        self.assertEqual(cuota, round(resultado,2))

    def Zero_rate(self):
        monto = 480000
        tasa = 0
        cuotas = 48
        cuota = 10000
        resultado = Payment.CalculateFee(monto, tasa, cuotas)

        self.assertEqual(cuota, round(resultado,2))

    def Usura(self):
        monto = 50000
        tasa = 12.4
        cuotas = 60

        try:
            resultado = Payment.CalculateFee(monto, tasa, cuotas)
            self.assertEqual(resultado, 0)
        except Payment.TasaExcesiva  :
            pass 

    def Usura_v2(self):
        monto = 50000
        tasa = 12.4
        cuotas = 60

        self.assertRaises(Payment.TasaExcesiva,  Payment.CalculateFee, monto, tasa, cuotas)

    def Single_fee(self):
        monto = 90000
        tasa = 2.4
        cuotas = 1
        cuota = 90000
        resultado = Payment.CalculateFee(monto, tasa, cuotas)

        self.assertEqual(cuota, round(resultado,2))

    def Buy_error(self):
        monto = 0
        tasa = 2.4
        cuotas = 60
        pass

    def Negative_error(self):
        monto = 50000
        tasa = 1
        cuotas = -10
        pass

if __name__ == '__main__':
    unittest.main()
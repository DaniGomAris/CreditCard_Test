import unittest
import Payment
import Exceptions

class CreditCardTest(unittest.TestCase):

    def normal_case(self):
        monto = 200000
        tasa = 3.1
        cuotas = 36
        cuota = 9297.96
        resultado = Payment.calculateFee(monto, tasa, cuotas)

        self.assertEqual(cuota, round(resultado,2))

    def normal_case_2(self):
        monto = 850000
        tasa = 3.4
        cuotas = 24
        cuota = 52377.5
        resultado = Payment.calculateFee(monto, tasa, cuotas)

        self.assertEqual(cuota, round(resultado,2))

    def zero_rate(self):
        monto = 480000
        tasa = 0
        cuotas = 48
        cuota = 10000
        resultado = Payment.calculateFee(monto, tasa, cuotas)

        self.assertEqual(cuota, round(resultado,2))

    def usura(self):
        monto = 50000
        tasa = 12.4
        cuotas = 60

        try:
            resultado = Payment.calculateFee(monto, tasa, cuotas)
            self.assertEqual(resultado, 0)
        except Exceptions.ExcessiveRate :
            pass 

    def usura_v2(self):
        monto = 50000
        tasa = 12.4
        cuotas = 60

        self.assertRaises(Exceptions.ExcessiveRate,  Payment.calculateFee, monto, tasa, cuotas)

    def single_fee(self):
        monto = 90000
        tasa = 2.4
        cuotas = 1
        cuota = 90000
        resultado = Payment.calculateFee(monto, tasa, cuotas)

        self.assertEqual(cuota, round(resultado,2))

    def buy_error(self):
        monto = 0
        tasa = 2.4
        cuotas = 60

        self.assertRaises(Exceptions.ZeroAmount, Payment.calculateFee, monto, tasa, cuotas)

    def negative_error(self):
        monto = 50000
        tasa = 1
        cuotas = -10

        self.assertRaises(Exceptions.NegativeShare, Payment.calculateFee, monto, tasa, cuotas)

if __name__ == '__main__':
    unittest.main()

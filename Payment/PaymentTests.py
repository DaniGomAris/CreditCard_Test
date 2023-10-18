import unittest
import Payment
import Exceptions

class CreditCardTest(unittest.TestCase):

    def normal_case(self):
        amount = 200000
        rate = 3.1
        pay = 36
        cuota = 9297.96
        resultado = Payment.CreditCardPayment.calculateFee(amount, rate, pay)

        self.assertEqual(cuota, round(resultado,2))


    def normal_case_2(self):
        amount = 850000
        rate = 3.4
        pay = 24
        cuota = 52377.5
        resultado = Payment.CreditCardPayment.calculateFee(amount, rate, pay)

        self.assertEqual(cuota, round(resultado,2))


    def zero_rate(self):
        amount = 480000
        rate = 0
        pay = 48
        cuota = 10000
        resultado = Payment.CreditCardPayment.calculateFee(amount, rate, pay)

        self.assertEqual(cuota, round(resultado,2))


    def usura(self):
        amount = 50000
        rate = 12.4
        pay = 60

        try:
            resultado = Payment.CreditCardPayment.calculateFee(amount, rate, pay)
            self.assertEqual(resultado, 0)
        except Exceptions.ExcessiveRate :
            pass 


    def usura_v2(self):
        amount = 50000
        rate = 12.4
        pay = 60

        self.assertRaises(Exceptions.ExcessiveRate,  Payment.CreditCardPayment.calculateFee, amount, rate, pay)


    def single_fee(self):
        amount = 90000
        rate = 2.4
        pay = 1
        cuota = 90000
        resultado = Payment.CreditCardPayment.calculateFee(amount, rate, pay)

        self.assertEqual(cuota, round(resultado,2))


    def buy_error(self):
        amount = 0
        rate = 2.4
        pay = 60

        self.assertRaises(Exceptions.ZeroAmount, Payment.CreditCardPayment.calculateFee, amount, rate, pay)


    def negative_error(self):
        amount = 50000
        rate = 1
        pay = -10

        self.assertRaises(Exceptions.NegativeShare, Payment.CreditCardPayment.calculateFee, amount, rate, pay)

if __name__ == '__main__':
    unittest.main()

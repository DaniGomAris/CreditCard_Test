import unittest
import Amortization
import Exceptions

class AmortizationPlanTest(unittest.TestCase):
    
    def only_fee(self):
        amount = 90000
        rate = 2.4
        pay = 1
        result = Amortization.CreditCardAmortizacion.amortizacion(amount, rate, pay)

        self.assertEqual(pay, round(result,2))
        

    def normal_case(self):
        amount = 9297
        rate = 3.1
        pay = 36
        result = Amortization.CreditCardAmortizacion.amortizacion(amount, rate, pay)

        self.assertEqual(pay, round(result,2))


    def normal_case_2(self):
        amount = 52377
        rate = 3.4
        pay = 24
        result = Amortization.CreditCardAmortizacion.amortizacion(amount, rate, pay)

        self.assertEqual(pay, round(result,2))


    def zero_rate(self):
        amount = 10000
        rate = 0
        pay = 48

        self.assertRaises(Exceptions.ZeroRate, Amortization.CreditCardAmortizacion.amortizacion, amount, rate, pay)


    def usura(self):
        amount = 6205
        rate = 12.4
        pay = 60

        self.assertRaises(Exceptions.ExcessiveRate, Amortization.CreditCardAmortizacion.amortizacion, amount, rate, pay)

if __name__ == '__main__':
    unittest.main()

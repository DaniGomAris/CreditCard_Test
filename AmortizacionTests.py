import unittest
import Amortizacion
import Exceptions

class AmortizationPlanTest(unittest.TestCase):
    
    def only_fee(self):
        monto = 90000
        tasa = 2.4
        cuotas = 1

    def normal_case(self):
        monto = 9297
        tasa = 3.1
        cuotas = 36

    def normal_case_2(self):
        monto = 52377
        tasa = 3.4
        cuotas = 24

    def zero_rate(self):
        monto = 10000
        tasa = 0
        cuotas = 48

    def usura(self):
        monto = 6205
        tasa = 12.4
        cuotas = 60

if __name__ == '__main__':
    unittest.main()
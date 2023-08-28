import unittest
import ExtraBonus
import Payment
import Exceptions

class BonusEffectTest(unittest.TestCase):

    def normal_case(self):
        monto = 200000
        tasa = 3.1
        cuotas = 36
        numero_cuota_a_abonar = 10
        abonoextra = 53000

    def normal_case_2(self):
        monto = 850000
        tasa = 3.4
        cuotas = 24
        numero_cuota_a_abonar = 5
        abonoextra = 90000

    def low_bonus_error(self):
        monto = 850000
        tasa = 3.4
        cuotas = 24
        numero_cuota_a_abonar = 10
        abonoextra = 45000

    def late_fee_error(self):
        monto = 850000
        tasa = 3.4
        cuotas = 24
        numero_cuota_a_abonar = 22
        abonoextra = 180000

if __name__ == '__main__':
    unittest.main()
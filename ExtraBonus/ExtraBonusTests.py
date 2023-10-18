import unittest

import ExtraBonus
import Exceptions

class BonusEffectTest(unittest.TestCase):

    def normal_case(self):
        amount = 200000
        rate = 3.1
        pay = 36
        number_pay_of_bonus = 10
        extrabonus = 53000
        result = ExtraBonus.CreditCardExtraBonus.extra_bonus(amount, rate, pay, number_pay_of_bonus, extrabonus)

        self.assertEqual(pay, round(result,2))


    def normal_case_2(self):
        amount = 850000
        rate = 3.4
        pay = 24
        number_pay_of_bonus = 5
        extrabonus = 90000
        result = ExtraBonus.CreditCardExtraBonus.extra_bonus(amount, rate, pay, number_pay_of_bonus, extrabonus)

        self.assertEqual(pay, round(result,2))


    def low_bonus_error(self):
        amount = 850000
        rate = 3.4
        pay = 24
        number_pay_of_bonus = 10
        extrabonus = 45000

        self.assertRaises(Exceptions.LowBonus, ExtraBonus.CreditCardExtraBonus.extra_bonus, amount, rate, pay, number_pay_of_bonus, extrabonus)


    def late_fee_error(self):
        amount = 850000
        rate = 3.4
        pay = 24
        number_pay_of_bonus = 22
        extrabonus = 180000

        self.assertRaises(Exceptions.Latefee, ExtraBonus.CreditCardExtraBonus.extra_bonus, amount, rate, pay, number_pay_of_bonus, extrabonus)
        
if __name__ == '__main__':
    unittest.main()

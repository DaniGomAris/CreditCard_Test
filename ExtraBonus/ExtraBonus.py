from Payment import Payment
import Exceptions

class CreditCardExtraBonus:

    def total_interests(amount: float, rate: float ,pay: int):
        quota_value = Payment.CreditCardPayment.calculateFee(amount, rate, pay)
        total_interests = (quota_value * pay) - amount
        return total_interests


    def extra_bonus(amount: float, rate: float , pay: int, number_pay_of_bonus: int, abonoextra: float):
        quota_value = Payment.CreditCardPayment.calculateFee(amount, rate, pay)
        print(quota_value)
        interests_x = rate/100
        balance = amount
        amortization_table = [["Cuota", "balance", "Pago interés", "Abono capital"], ["#", quota_value, rate, amount]]
        if pay == 1:
            pay_number = 1
            interests = (rate * balance) / 100
            abono_capital = quota_value - interests
            row = [pay_number, balance, interests, abono_capital]
            amortization_table.append(row)
        else:
            for cuota in range(1, pay + 1):
                if balance <=0:
                    break

                pay_number = cuota
                interests = interests_x * balance

                if number_pay_of_bonus == pay_number:
                    cuota_real_a_abonar = abonoextra
                else:
                    cuota_real_a_abonar = quota_value
            
                abono_capital = cuota_real_a_abonar - interests
                balance -= abono_capital

                if abonoextra < cuota_real_a_abonar:
                    raise Exceptions.LowBonus
                
                if abonoextra > balance:
                    raise Exceptions.HighBonus

                if balance < 0:
                    abono_capital += balance + interests
                    balance = 0

                row = [pay_number, balance, interests, abono_capital]
                amortization_table.append(row)

            if balance < abono_capital:
                    abono_capital = balance

        return amortization_table

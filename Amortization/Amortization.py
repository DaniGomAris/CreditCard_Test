from Payment import Payment

class CreditCardAmortizacion:

    def total_Interest(amount: float, rate: float ,pay: int):
        payment_value = Payment.CreditCardPayment.calculateFee(amount, rate, pay)
        total_interests = (payment_value * pay) - amount
        return total_interests


    def amortizacion(amount: float, rate: float ,pay: int):
        payment_value = Payment.CreditCardPayment.calculateFee(amount, rate, pay)
        print(payment_value)
        interests_x = rate/100
        balance = amount
        amortizacion_table = [["payment", "balance", "Interest pay", "Capital bonus"], ["#", payment_value, rate, amount]]

        if pay == 1:
            payment_number = 1
            interests = (rate * balance) / 100
            capital_bonus = payment_value - interests
            row = [payment_number, balance, interests, capital_bonus]
            amortizacion_table.append(row)
        else:
            for payment in range(1, pay + 1):
                payment_number = payment
                interests = interests_x * balance
                capital_bonus = payment_value - interests
                balance = balance - capital_bonus
                row = [payment_number, balance, interests, capital_bonus]
                amortizacion_table.append(row)
                print(row)
        return amortizacion_table

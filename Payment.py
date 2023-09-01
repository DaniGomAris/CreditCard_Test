import Exceptions
from abc import ABC

class CreditCardPayment(ABC):
    
    def calculateFee(amount: float, rate: float, pay: int):
        p =  rate / 100
        if amount == 0:
            raise Exceptions.ZeroAmount("El monto es 0")
        if rate*12 > 100 :
            raise Exceptions.ExcessiveRate("La tasa no debe ser superior a 100")
        if pay <= 0:
            raise Exceptions.NegativeShare("Las cuotas son menores o iguales a 0")
        if pay == 1 :
            return amount
        if rate == 0:
            return amount / pay
        else:         
            return (amount * p) / (1 - (1 + p) ** (-pay))

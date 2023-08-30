import Exceptions
from abc import ABC

class CreditCardPayment(ABC):
    
    def calculateFee(monto,tasa,cuotas):
        p =  tasa / 100
        if monto == 0:
            raise Exceptions.ZeroAmount("El monto es 0")
        if tasa*12 > 100 :
            raise Exceptions.ExcessiveRate("La tasa no debe ser superior a 100")
        if cuotas <= 0:
            raise Exceptions.NegativeShare("Las cuotas son menores o iguales a 0")
        if cuotas == 1 :
            return monto
        if tasa == 0:
            return monto / cuotas
        else:         
            return (monto * p) / (1 - (1 + p) ** (-cuotas))

class ExcessiveRate(Exception): 
    pass

class NegativeShare(Exception):
    pass

class ZeroAmount(Exception):
    pass

class LowBonus(Exception):
    pass

class HighBonus(Exception):
    pass

def calculateFee(monto,tasa,cuotas):
    p =  tasa / 100
    if monto == 0:
        raise ZeroAmount("El monto es 0")
    if tasa*12 > 100 :
        raise ExcessiveRate("La tasa no debe ser superior a 100")
    if cuotas <= 0:
        raise NegativeShare("Las cuotas son menores o iguales a 0")
    if cuotas == 1 :
        return monto
    if tasa == 0:
        return monto / cuotas
    else:         
        return (monto * p) / (1 - (1 + p) ** (-cuotas))
    

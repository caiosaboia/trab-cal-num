import math
def phi(q, c):
    return math.sqrt(c * math.exp(q)/4)

def funcao(x, C):
    return C*math.exp(x) - 4*x**2
   
def derivada(x, C):
    return C*math.exp(x) -4*2*x
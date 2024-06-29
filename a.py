import math
def ponto_fixo(phi, c, x0, erro, max_iter):
    if abs(phi(x0, c)) < erro:
            return x0
    
    k = 0
    while k < max_iter:
        x = phi(x0, c)
        print(f"valor de X = {x}")
        if abs(phi(x, c)) < erro or abs(x - x0) < erro:
            return x
        
        x0 = x
        k =+ 1

        print(f"valor de X0 = {x0}") #visualizar iteração
    return x



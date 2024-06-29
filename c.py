import math
from funcoes import funcao

# Método recebe a função f, chutes iniciais x0 e x1, dois erros e iteração máxima
def secante(func, C, x0, x1, err1, err2, max_iter):
    # Se o chute inicial x0 já estiver perto do 0 retornar x0
    if abs(func(x0, C)) < err1:
            return x0
     # Se o chute inicial x0 já estiver perto do 0 retornar x0
    if abs(func(x1, C)) < err1 or abs(x1 - x0) < err2:
            return x1
    # Se não, executar secante recorrentemente
    k = 0
    while k < max_iter:
        # Executa a iteração
        x2 = x1 - (func(x1, C) * (x1-x0)) / (func(x1, C) - func(x0, C))
        # Verifica se convergiu se f(x) é menor que o erro ou |x-x_anterior| é menor que o erro
        if abs(func(x2, C)) < err1 or abs(x2 - x1) < err2:
            # Se for, retorna x
            return x2
        # O x atual será o anterior da próxima iteração    
        x0 = x1
        x1 = x2
        # Incrementa o contador
        k = k + 1
        print(f"Esse é o valor de x0: {x0}")
    return x1



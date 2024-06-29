import math
from funcoes import funcao, derivada
# Método recebe a função f, a derivada da função f, o chute inicial x0, um erro e iteração máxima
def newtonrhapson(f, C, derivf, x0, err, max_iter):
    # Se o chute inicial x0 já estiver perto do 0 retornar x0
    if abs(funcao(x0, C)) < err:
            return x0
    # Se não, executar newton-rhapson recorrentemente
    k = 0
    while k < max_iter:
        # Derivada (denominador) não pode ser zero
        if derivada(x0, C) == 0:
            return print("Derivada igual a zero")
        # Executa a iteração
        x = x0 - funcao(x0, C) / derivada(x0, C)
        # Verifica se convergiu se f(x) é menor que o erro ou |x-x_anterior| é menor que o erro
        if abs(funcao(x, C)) < err or abs(x - x0) < err:
            # Se for, retorna x
            return x
        # O x atual será o anterior da próxima iteração    
        x0 = x
        # Incrementa o contador
        k = k + 1

        print(f"Valor de x0:{x0}")
    return x



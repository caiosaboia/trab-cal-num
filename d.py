from a import ponto_fixo
from b import newtonrhapson
from c import secante
from funcoes import phi, funcao, derivada

def verifica_prejuizo(valor, limite):
    if valor > limite:
        print("Está saindo no prejuízo.")
    else:
        print("Está no lucro.")


#Teste do Ponto Fixo
print("Teste do Ponto Fixo")
x0 = 0.5
c = 1
erro = 1e-4
raiz = ponto_fixo(phi, c, x0, erro, max_iter=1000)
verifica_prejuizo(raiz, 0.7)
print("\n")

#Teste do NewtonRhapson
print("Teste do NewtonRhapson")
max_iter = 1000
F = funcao(x0, c)
Dev = derivada(x0, c)
raiz2 = newtonrhapson(F, c, Dev, x0, erro, max_iter)
verifica_prejuizo(raiz2, 0.7)
print("\n")

#Teste da Secante
print("Teste da Secante")
x1 = 0.1
err1 = 1e-6
err2 = 1e-5
fun = lambda x0, c: funcao(x0, c)
raiz3 = secante(fun, c,x0, x1, err1, err2, max_iter)
verifica_prejuizo(raiz3, 0.7)
print("\n")


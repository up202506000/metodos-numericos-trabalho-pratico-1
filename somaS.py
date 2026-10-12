import math
def somaS(eps):
    soma = 0.0
    termo = 9.0 #0.5*18
    fator_majorante = 4/3 #1/(1-L) L=1/4
    n=0 #numero de iteracoes
    k=1 #valor da iteracao da soma

    while True:
        soma += termo
        n+=1

        termo_seguinte = termo * (k**2)/((2*k+1)*(2*k+2))
        erro_majorado = termo_seguinte * fator_majorante
        if erro_majorado < eps:
            break

        k += 1
        termo = termo_seguinte

    return n, soma

for expoente in range(8,16):
    eps = 10**-expoente
    n,resultado_S = somaS(eps)
    erro_efetivo = abs(math.pi**2 - resultado_S)
    print(f"Epsilon = 10^-{expoente}  n={n}  resultado = {resultado_S}  Erro absoluto efetivo = {erro_efetivo}")


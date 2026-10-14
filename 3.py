
def a_euler(n):
    return (1+1/n)**n


for j in range(1,17):
    n = 10**j
    res = a_euler(n)
    print(f"10^{j}   resultado = {res}")


def b_euler(m):
    soma = 0.0
    termo = 1.0
    k = 0

    while (k<=m):
        soma += termo

        termo = termo * (1/ (k+1))
        k +=1

    return soma

for m in range(1,21):
    res = b_euler(m)
    print(f"m={m}   resultado = {res}")

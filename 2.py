import math

def u(eps):
    acc = 0.0
    ter = 9.0
    err = math.inf
    rnd = 0.0
    k = 1
    while (err > eps and k < 50):
        acc += ter
        ter *= (k ** 2) / ((2*k + 1) * (2*k + 2))
        err = (4/3) * ter + rnd
        k += 1
    return k - 1, acc, abs(math.pi**2 - acc)

for i in range(8, 16):
    res = u(10**(-i))
    print(f"n = {res[0]} | val = {res[1]} | err = {res[2]}")
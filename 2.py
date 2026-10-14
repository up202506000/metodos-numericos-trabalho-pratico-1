import math

def S(eps):
    acc = 0.0
    ter = 9.0
    err = math.inf
    k = 1
    while (err > eps and k < 25):
        acc += ter
        ter *= (k ** 2) / ((2*k + 1) * (2*k + 2))
        err = (4/3) * ter
        k += 1
    return k - 1, acc, abs(math.pi**2 - acc)

for i in range(8, 16):
    res = S(10**(-i))
    print("----------------------------------------------------------------")
    print(f"n   = {res[0]}")
    print(f"val = {res[1]}")
    print(f"err = {res[2]}")
    print(f"eps = 10^(-{i})")
print("----------------------------------------------------------------")
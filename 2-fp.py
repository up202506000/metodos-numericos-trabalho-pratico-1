from fp import *
import math

def S(eps):
    acc = FP(0.0)
    ter = FP(9.0)
    err = FP(math.inf)
    k = 1
    while (err > eps):
        acc += ter
        ter *= FP(k ** 2) / ((2*k + 1) * (2*k + 2))
        err = FP(4/3) * ter
        k += 1
    return (
        k - 1,
        acc,
        err,
        math.nextafter(abs(math.pi**2 - float(acc)), math.inf)
    )

for i in range(8, 16):
    res = S(10**(-i))
    print("----------------------------------------------------------------")
    print(f"n      = {res[0]}")
    print(f"val    = {res[1]}")
    print(f"errUpb = {res[2]}")
    print(f"errAbs = {res[3]}")
    print(f"eps    = 10^(-{i})")
print("----------------------------------------------------------------")
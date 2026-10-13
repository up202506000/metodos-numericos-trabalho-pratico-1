import math

def S(eps):
    acc = 0.0
    ter = 9.0
    err = math.inf
    k = 1
    while (err > eps and k < 50):
        acc += ter
        ter *= (k ** 2) / ((2*k + 1) * (2*k + 2))
        err = (4/3) * ter
        k += 1
    return k - 1, acc, abs(math.pi**2 - acc)

for i in range(8, 16):
    res = S(10**(-i))
    s = str(res[2]).split("e")
    print("$10^-{" + str(i) + "}$ & " + str(res[0]) + " & " + str(res[1]) + " & $" + s[0] + " \\times 10^" + s[1] + "$ \\\\ \\hline")
import math
import bisect

def S(eps):

    # Variables
    lst = []
    ter = 9.0
    err = math.inf
    k = 1
    res = 0.0

    # Calculate terms
    while (err > eps and k < 25):
        lst.append(ter)
        ter *= (k**2) / ((2*k + 1) * (2*k + 2))
        err = (4/3) * ter
        k += 1

    # Remove 2 smallest and insert their sum until 1 remains
    lst.sort(key = abs)
    while len(lst) > 1:
        res = lst[0] + lst[1]
        lst = lst[2:]
        bisect.insort(lst, res, key = abs)

    # Return number of iterations, result and absolute error
    return (
        k - 1,
        res,
        abs(math.pi**2 - res)
    )

# Tests
for i in range(8, 16):
    res = S(10**(-i))
    print("----------------------------------------------------------------")
    print(f"n   = {res[0]}")
    print(f"val = {res[1]}")
    print(f"err = {res[2]}")
    print(f"eps = 10^(-{i})")
print("----------------------------------------------------------------")
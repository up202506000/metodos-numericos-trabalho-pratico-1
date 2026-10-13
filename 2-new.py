import math
import bisect

def u(eps):

    # Variables
    lst = []
    ter = 9.0
    err = math.inf
    top = 1
    bot = 1
    k = 1
    res = 0.0

    # Calculate terms
    while (err > eps and k < 25):
        ter = (9 * top) / bot
        lst.append(ter)
        top *= k ** 2
        bot *= (2*k + 1) * (2*k + 2)
        err = (4/3) * ter
        k += 1

    # Remove 2 smallest and insert their sum until 1 remains
    lst.sort()
    while len(lst) > 1:
        res = lst[0] + lst[1]
        lst = lst[2:]
        bisect.insort(lst, res)
    res = lst[0]

    # Return number of iterations, result and absolute error
    # (The absolute error is given with respect to the double
    # precision representation of pi^2 and not pi^2 itself)
    return (
        k - 1,
        res,
        abs(math.pi**2 - res)
    )

# Tests
for i in range(8, 16):
    res = u(10**(-i))
    print("----------------------------------------------------------------")
    print(f"n   = {res[0]}")
    print(f"val = {res[1]}")
    print(f"err = {res[2]}")
    print(f"eps = 10^(-{i})")
print("----------------------------------------------------------------")
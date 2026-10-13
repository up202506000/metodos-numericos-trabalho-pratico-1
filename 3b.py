import math

def b(n):
    term = 1.0
    acc = 0
    for k in range(n):
        acc += term
        term *= 1 / (k + 1)
    return acc

res = 0.0
for i in range(1, 21):
    res = b(i)
    print("---------------------------------")
    print(f"val = {res}")
    print(f"err = {abs(math.e - res)}")
print("---------------------------------")
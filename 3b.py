import math

def b(n):
    term = 1.0
    acc = 0
    for k in range(n):
        acc += term
        term *= 1 / (k + 1)
    return acc

for i in range(1, 21):
    print(b(i))

print()
print(math.e)
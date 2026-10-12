
def epsilon():
    eps = 1.0

    while 1 + eps > 1:
        eps /= 2

    return eps*2

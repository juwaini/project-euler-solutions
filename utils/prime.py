import math


def is_prime(x):
    if x in [0, 1]:
        return False
    if x in [2, 3]:
        return True

    for n in range(2, int(math.sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True

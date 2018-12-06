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


def is_truncatable_prime(n):
    length_n = len(str(n))
    if length_n < 2:
        return False

    for i in range(length_n):
        if not is_prime(int(str(n)[i:])):
            return False

    for i in range(length_n - 1):
        # print(str(n)[:-(i + 1)])
        if not is_prime(int(str(n)[:-(i + 1)])):
            return False

    return True

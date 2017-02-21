import math


def is_prime(x):
    for n in range(2, int(math.sqrt(x))):
        if x%n == 0:
            return False
    return True


def is_factor(n, x):
    if n % x == 0:
        return True
    else:
        return False


def get_prime_factors(n):
    prime_factors = []
    for x in range(2, int(math.sqrt(n))):
        if is_prime(x):
            if is_factor(n, x):
                prime_factors.append(x)
    return prime_factors


if __name__ == '__main__':
    n = 13195
    print("Prime factors for", n , " is ", get_prime_factors(n))

    c = 600851475143
    print("The biggest prime factors for", c, " is ", max(get_prime_factors(c)))


import math


def primes_up_to(n):
    primes = [2]
    for i in range(3, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(primes_up_to(100))
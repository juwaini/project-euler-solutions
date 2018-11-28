import math
import pprint


def is_prime(x):
    if x in [0, 1]:
        return False
    for n in range(2, int(math.sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True


if __name__ == '__main__':
    primes = []
    for i in range(1488, 10_000):
        if is_prime(i):
            primes.append(i)

    for x in range(0, len(primes)):
        for y in range(x+1, len(primes)):
            z = primes[y] + (primes[y] - primes[x])
            if z in primes and (set(str(primes[x])) == set(str(primes[y])) == set(str(z))):
                print(f'{primes[x]}{primes[y]}{z}')
                break

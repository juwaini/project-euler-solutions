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
    primes_100 = primes_up_to(100)
    total = 0
    count = 0
    flag = True

    while flag:
        if is_prime(sum(primes_100)):
            print(f'{primes_100}: {sum(primes_100)} - {len(primes_100)}')
            flag = False
        else:
            print(f'{primes_100}: {sum(primes_100)} - {len(primes_100)}')
            primes_100.pop(-1)

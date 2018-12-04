import math

from utils.prime import is_prime


def number_of_divisors(number):
    if number in [0, 1]:
        return 0

    if is_prime(number):
        return 2

    factors = 0
    upper_limit = int(math.sqrt(number + 1))

    for i in range(1, upper_limit):
        if number % i == 0:
            factors += 1

    return factors*2


def get_all_divisors(number):
    all_divisors = set()
    upper_limit = math.ceil(math.sqrt(number))

    for i in range(1, upper_limit):
        if number % i == 0:
            all_divisors.add(i)
            all_divisors.add(int(number/i))

    return sorted(list(all_divisors))

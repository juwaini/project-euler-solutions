import math


def is_prime(x):
    if x in [0, 1]:
        return False
    for n in range(2, int(math.sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True


def get_all_prime_factors(n):
    prime_factors = set()

    for x in range(2, n + 1):
        if (n % x == 0) and (is_prime(x)) and (is_prime(int(n/x))):
            prime_factors.add(x)
            prime_factors.add(int(n/x))

    return prime_factors


def first_n_with_n_distinct_prime_factors(n):
    ns = []
    count = 0
    low_limit = int('1' + '0'*(n-1))
    upper_limit = int('1' + '0'*n)

    print(f'{low_limit} -> {upper_limit}')
    for i in range(low_limit, upper_limit):
        if len(get_all_prime_factors(i)) == n:
            count += 1
            ns.append(i)

            if count == n:
                return ns
        else:
            count = 0
            ns.clear()


if __name__ == '__main__':
    print(first_n_with_n_distinct_prime_factors(2))
    # print(get_all_prime_factors(645))
    # print(first_n_with_n_distinct_prime_factors(3))
    print(first_n_with_n_distinct_prime_factors(4))

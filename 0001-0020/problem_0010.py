from .problem_0003 import is_prime


def sum_of_all_primes_below_n(n):
    total = 0
    for i in range(2, n+1):
        if is_prime(i):
            total += i
    return total


if __name__ == '__main__':
    print('Sum of all primes under 10 is %d.' % sum_of_all_primes_below_n(10))
    print('Sum of all primes under 2_000_000 is %d.' % sum_of_all_primes_below_n(2_000_000))

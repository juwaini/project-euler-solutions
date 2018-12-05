from utils.prime import is_prime
from itertools import permutations


def is_circular_prime(n):
    str_n = list(str(n))
    perm = set(list(permutations(str_n)))
    for p in perm:
        if not is_prime(int(''.join(p))):
            print(int(''.join(p)))
            return False
    return True


if __name__ == '__main__':
    assert is_circular_prime(197)

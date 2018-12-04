from math import sqrt
from .problem_0003 import is_prime


def generate_triangle_number(n):
    triangle_number = sum(range(1, n+1))
    return triangle_number


def get_total_factors(n):
    factor = 0
    for i in range(1, int(sqrt(n+1))):
        if n % i == 0:
            factor += 1
    # print(f'number of factors for {n}: {factor*2}')
    return 2*factor


if __name__ == '__main__':
    factors = 0
    tri_no = 1
    while factors <= 500:
        number = generate_triangle_number(tri_no)
        if not is_prime(number):
            factors = get_total_factors(number)
        tri_no += 1
    print(number)

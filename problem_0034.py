import math


def sum_of_factorial_digit(n):
    total = sum([math.factorial(int(dig)) for dig in list(str(n))])
    if total == n:
        return total
    else:
        return 0


if __name__ == '__main__':
    tot = 0
    for i in range(4, 1_000_000):
        tot += sum_of_factorial_digit(i)
    print(tot)

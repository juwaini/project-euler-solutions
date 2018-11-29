import math


def lattice(n):
    upper = math.factorial(2*n)
    lower = math.factorial(n)*math.factorial(n)
    print(int(upper/lower))
    return int(upper / lower)


if __name__ == '__main__':
    lattice(1)
    lattice(2)
    lattice(3)
    lattice(20)

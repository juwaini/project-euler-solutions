from utils.divisor import number_of_divisors

NUM_OF_DIV = 8


def f(n):
    cnt = 0
    lst = list()
    for x in range(1, n+1):
        if number_of_divisors(x) == NUM_OF_DIV:
            cnt += 1
            lst.append(x)
    return cnt, lst


if __name__ == '__main__':
    # print(number_of_divisors(24))
    print(f(100))
    print(f(1000))
    # print(f(10**6))

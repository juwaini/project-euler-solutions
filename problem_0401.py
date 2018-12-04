from utils.divisor import get_all_divisors


def sigma2(number):
    ls = get_all_divisors(number)
    all_squares = [i*i for i in ls]
    return sum(all_squares)


if __name__ == '__main__':
    assert get_all_divisors(6) == [1, 2, 3, 6]
    assert sigma2(6) == 50

from math import pow


def get_all_integer_combination(a, b):
    all_product = [
        pow(i, j)
        for i in range(2, a+1)
        for j in range(2, b+1)
    ]

    all_product = set(all_product)
    return len(all_product)


if __name__ == '__main__':
    a = 5
    b = 5
    print(f'There are {get_all_integer_combination(a, b)} distinct terms for {a} and {b}.')

    a = 100
    b = 100
    print(f'There are {get_all_integer_combination(a, b)} distinct terms for {a} and {b}.')
def sum_of_the_digits(n):
    product = str(2**n)
    total = sum([int(i) for i in product])
    print(total)
    return total


if __name__ == '__main__':
    sum_of_the_digits(15)
    sum_of_the_digits(1000)

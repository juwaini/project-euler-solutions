def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)


def sum_of_the_digit(number):
    number = str(number)
    return sum([int(num) for num in number])


if __name__ == '__main__':
    n = 10
    print(f'Sum of the digits for {n}! is {sum_of_the_digit(factorial(n))}')

    n = 100
    print(f'Sum of the digits for {n}! is {sum_of_the_digit(factorial(n))}')

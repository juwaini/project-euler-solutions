

def sum_of_the_squares_of_the_first_n(n):
    total = 0
    for i in range(1, n+1):
        total += i*i
    return total


def square_of_the_sum_of_the_first_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total*total

if __name__ == '__main__':
    n = 10
    a = sum_of_the_squares_of_the_first_n(n)
    b = square_of_the_sum_of_the_first_n(n)
    print('%d - %d = %d.' % (b, a, b-a))

    n = 100
    a = sum_of_the_squares_of_the_first_n(n)
    b = square_of_the_sum_of_the_first_n(n)
    print('%d - %d = %d.' % (b, a, b-a))
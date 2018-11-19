def get_sum_of_n_multiples_under_x(x):
    ls = []
    for i in range(0, x):
        if i%3 == 0 or i%5 == 0:
            ls.append(i)

    print("Sum of all 3 and 5 multiples under %d is: %d" % (x, sum(ls)))


if __name__ == '__main__':
    get_sum_of_n_multiples_under_x(10)
    get_sum_of_n_multiples_under_x(1000)

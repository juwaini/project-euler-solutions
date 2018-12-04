def sum_of_spiral_diagonals(n):
    if n % 2 == 0:
        return 0

    number_of_terms = 2*n - 1
    print(f'Number of terms for {n} is: {number_of_terms}')
    skip = 1
    ls_of_diagonals = [1]
    for i in range(1, number_of_terms):
        ls_of_diagonals.append(ls_of_diagonals[-1] + (skip * 2))
        if i % 4 == 0:
            skip += 1

    #  print(ls_of_diagonals)
    return sum(ls_of_diagonals)


if __name__ == '__main__':
    print(f'{sum_of_spiral_diagonals(1)}')
    print(f'{sum_of_spiral_diagonals(3)}')
    print(f'{sum_of_spiral_diagonals(5)}')
    print(f'{sum_of_spiral_diagonals(1001)}')


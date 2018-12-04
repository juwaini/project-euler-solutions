import pdb


def get_max_sum_of_4_neighbouring_number_in_list(ls):
    sum_ls = []
    if len(ls) < 4:
        return 0
    else:
        for i in range(0, len(ls)-3):
            sum_ls.append(ls[i] * ls[i+1] * ls[i+2] * ls[i+3])
        return max(sum_ls)


if __name__ == '__main__':

    file = open('files/problem_0011_20_by_20_grid', 'r')
    matrix = []
    inner_list = []
    for line in file:
        for number in line.split(' '):
            inner_list.append(int(number))
        matrix.append(inner_list)
        inner_list = []

    sum_horizontal = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)-4):
            sum_horizontal.append(matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3])

    max_horizontal = max(sum_horizontal)
    print('max_horizontal = ', max_horizontal)

    sum_vertical = []
    for i in range(0, len(matrix)-4):
        for j in range(0, len(matrix)):
            sum_vertical.append(matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j])

    max_vertical = max(sum_vertical)
    print('max_vertical = ', max_vertical)

    idx = 1
    sum_diagonal_left = []
    for n in range(0, 39):
        matrix_to_list = []
        if n <= 19:
            x = n
            y = 0
            while x >= 0:
                matrix_to_list.append(matrix[x][y])
                x -= 1
                y += 1
        else:
            x = 19
            y = n-19
            while x >= n-19:
                matrix_to_list.append(matrix[x][y])
                x -= 1
                y += 1
        print(idx, 'list to send: ', matrix_to_list)
        idx += 1

        sum_diagonal_left.append(get_max_sum_of_4_neighbouring_number_in_list(matrix_to_list))

    max_diagonal_left = max(sum_diagonal_left)
    print('max_diagonal_left = ', max_diagonal_left)

    print('max = ', max(max_horizontal, max_vertical, max_diagonal_left))

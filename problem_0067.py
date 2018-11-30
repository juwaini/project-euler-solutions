def convert_triangle(filename):
    example_list = []
    with open(filename) as file:
        for line in file:
            vals = line.split(' ')
            example_list.append([int(v) for v in vals])
    # pprint.pprint(example_list)
    return example_list


def solution(t):
    for i in range(len(t) - 2, 0, -1):
        for j in range(0, len(t[i]), 1):
            t[i][j] += max(t[i+1][j], t[i+1][j+1])
            # print(f'at t[{i}][{j}]: {t[i][j]}')
    t[0][0] += max(t[1][0], t[1][1])
    return t[0][0]


if __name__ == '__main__':
    triangle_example = convert_triangle('files/problem_67_example')
    print(solution(triangle_example))

    tri_problem = convert_triangle('files/p067_triangle.txt')
    print(solution(tri_problem))

def is_pandigital(i, j):
    str_concat = str(i) + str(j) + str(i*j)
    if (
            len(str_concat) == 9
    ) and (
            set(str_concat) - set(list('123456789')) == set()
    ):
        return True
    return False


if __name__ == '__main__':
    all_pandigitals = []
    for i in range(1, 1_000):
        for j in range(1_000, 10_0000):
            if is_pandigital(i, j):
                all_pandigitals.append(i*j)
    print(sum(set(all_pandigitals)))

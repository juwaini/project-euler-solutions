from utils.prime import is_prime


def generate_circular(n):
    number_of_circular = len(str(n))
    circulars = [n]

    for i in range(number_of_circular - 1):
        str_n = list(str(circulars[i]))
        if ('2' in str_n) or ('5' in str_n) or ('0' in str_n):
            return []

        tmp = str_n[0]
        for j in range(len(str_n)):
            if j == len(str_n) - 1:
                str_n[j] = tmp
            else:
                str_n[j] = str_n[j+1]

        circulars.append(int(''.join(str_n)))

    return circulars


def is_circular_prime(n):
    circs = generate_circular(n)

    if not circs:
        return False

    for p in circs:
        if not is_prime(p):
            return False

    # print(circs)
    return True


if __name__ == '__main__':
    assert is_circular_prime(197)

    cp = set()
    for i in range(2, 101):
        if is_circular_prime(i):
            cp.add(i)
    print(sorted(cp), len(cp))

    cp = set()
    for i in range(2, 1_000_001):
        if is_circular_prime(i):
            cp.add(i)
    print(sorted(cp), len(cp))

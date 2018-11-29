def sequence(n):
    seq = n
    terms = 1
    while n != 1:
        if n % 2:  # is odd
            n = 3*n + 1
        else:
            n = n/2

        terms += 1
    # print(f'sequence({seq}) has {terms} term(s).')
    return seq, terms


if __name__ == '__main__':
    # sequence(13)
    tmp_s = 0
    tmp_t = 0
    for i in range(1, 1_000_001):
        s, t = sequence(i)
        if t > tmp_t:
            tmp_s = s
            tmp_t = t

    print(f'Final s: {tmp_s}, final t: {tmp_t}')

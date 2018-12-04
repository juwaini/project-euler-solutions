from utils.divisibility import streak


def P(s, N):
    count = 0
    for n in range(2, N):
        if streak(n) == s:
            count += 1
    return count


if __name__ == '__main__':
    print(f'streak(13): {streak(13)}')
    print(f'streak(120): {streak(120)}')
    print(f'P(3, 14): {P(3, 14)}')
    print(f'P(6, 10**6): {P(6, 10**6)}')

    total = 0
    for i in range(1, 32):
        total += P(i, 4**i)
    print(f'sum of total: {total}')

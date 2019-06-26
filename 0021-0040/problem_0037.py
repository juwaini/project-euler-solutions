from utils.prime import is_prime, is_truncatable_prime

if __name__ == '__main__':
    assert not is_truncatable_prime(13)
    assert is_truncatable_prime(3797)

    count = 0
    total = 0
    all_truncs = []
    i = 11
    while count != 11:
        if is_prime(i):
            if is_truncatable_prime(i):
                count += 1
                total += i
                all_truncs.append(i)

        i += 1
    print(all_truncs)
    print(f'sum of all: {sum(all_truncs)}')



def is_divisible_by_1_to_10(n):
    for x in range(1, 11):
        if n % x != 0:
            return False
    return True

def is_divisible_by_1_to_20(n):
    for x in range(1, 21):
        if n % x != 0:
            return False
    return True

if __name__ == '__main__':
    i = 11
    while not is_divisible_by_1_to_10(i):
        i += 1
    print('%d is divisible by 1-10' % i)

    i = 21
    while not is_divisible_by_1_to_20(i):
        i += 1
    print('%d is divisible by 1-20' % i)
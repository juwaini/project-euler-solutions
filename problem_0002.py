def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    fibo_number = [1, 2]
    while fibo_number[-1] <= 4000000:
        fibo_number.append(fibo_number[-1] + fibo_number[-2])

    total = 0
    for fn in fibo_number:
        if is_even(fn):
            total += fn
    print("The sum of even-valued fibo number that less than 4 million is: %d" % total)
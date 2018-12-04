def streak(n):
    divide = 1
    count = 0

    while True:
        if n % divide == 0:
            divide += 1
            n += 1
            count += 1
        else:
            return count

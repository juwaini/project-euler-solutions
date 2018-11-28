if __name__ == '__main__':
    # n = 125874
    # n2 = n*2
    #
    # assert set(str(n)) == set(str(n2))

    n = 1
    while True:
        if set(str(n)) == set(str(n*2)) == set(str(n*3)) == set(str(n*4)) \
                == set(str(n*5)) == set(str(n*6)):
            print(n)
            break
        else:
            n += 1

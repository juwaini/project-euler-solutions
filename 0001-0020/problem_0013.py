if __name__ == '__main__':

    total = 0
    file = open('files/problem13.txt', 'r')
    for line in file:
        total += int(line)

    print(str(total)[:10])

if __name__ == '__main__':
    for c in range(1000, 1, -1):
        for b in range(c-1, 1, -1):
            for a in range(b-1, 1, -1):
                if (a + b + c == 1000) and (a*a + b*b == c*c):
                    print('%d + %d + %d = 1000' % (a, b, c))
                    print('%d^2 + %d^2 = %d^2' % (a, b, c))
                    print('a*b*c == ', a*b*c)

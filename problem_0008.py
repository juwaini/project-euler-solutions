

def get_biggest_product_of_n_adjacent_digit_in_s(s, n):
    biggest_product = []
    for i in range(0, len(s) - n):
        product = int(s[i])
        for x in range(1, n):
            product *= int(s[i+x])
        biggest_product.append(product)
    return max(biggest_product)


if __name__ == '__main__':
    file = open('files/1000_digit_number.txt', 'r')
    buffer = file.read()

    n = 4
    biggest = get_biggest_product_of_n_adjacent_digit_in_s(buffer, n)
    print('The biggest product for %d adjacent digit is: %d' % (n, biggest))

    n = 13
    biggest = get_biggest_product_of_n_adjacent_digit_in_s(buffer, n)
    print('The biggest product for %d adjacent digit is: %d' % (n, biggest))
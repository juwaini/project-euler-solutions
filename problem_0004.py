import math


def is_palindrome(s):
    for x in range(0, math.floor(len(s)/2)):
        if s[x] != s[-(x+1)]:
            return False
    return True


def generate_product_as_string(x, y):
    return str(x*y)


if __name__ == '__main__':
    palindrome_list = []
    for i in range(10, 100):
        for j in range(10, 100):
            product = str(i*j)
            if is_palindrome(product):
                palindrome_list.append(i*j)
    print("Largest palindrome made from product of 2 digit number: %d" % max(palindrome_list))

    palindrome_list = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = str(i*j)
            if is_palindrome(product):
                palindrome_list.append(i*j)
    print("Largest palindrome made from product of 3 digit number: %d" % max(palindrome_list))

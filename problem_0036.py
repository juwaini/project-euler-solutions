from utils.palindrome import is_palindrome


if __name__ == '__main__':
    assert is_palindrome(585)
    assert is_palindrome(str(bin(585))[2:])

    totals = 0
    for i in range(0, 1_000_000):
        if is_palindrome(i) and is_palindrome(str(bin(i))[2:]):
            totals += i

    print(totals)

def is_palindrome(s):
    if type(s) != str:
        s = str(s)

    for i in range(0, (len(s)//2) + 1):
        if s[i] != s[-(i + 1)]:
            return False

    return True


if __name__ == '__main__':
    assert is_palindrome(131)
    assert is_palindrome(100010001)
    assert is_palindrome('drawkward')

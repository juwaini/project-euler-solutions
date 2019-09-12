def is_palindrome(s):
    if type(s) != str:
        s = str(s)

    # for i in range(0, (len(s)//2) + 1):
    #     if s[i] != s[-(i + 1)]:
    #         return False
    # return True

    while s[0] == s[-1]:
        if len(s) == 1 or s == '':
            return True
        else:
            s = s[1:-1]
    return False


if __name__ == '__main__':
    assert is_palindrome(131) == True
    assert is_palindrome(100010001) == True
    assert is_palindrome('drawkward') == True

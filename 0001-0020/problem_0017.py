def map_number_to_words(n):
    words = ''
    n_digit = len(str(n))
    if n_digit == 1:
        words = single_digit(n)
    elif n_digit == 2:
        words = double_digit(n)
    elif n_digit == 3:
        words = triple_digit(n)

    # print(words)
    return words


def single_digit(digit):
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return words[digit - 1]


def double_digit(digit):
    dig = str(digit)
    words_teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                  'nineteen']
    words = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if dig[0] == '1':
        return words_teen[digit - 10]
    elif dig[0] != '1' and dig[1] == '0':
        return words[int((digit - 20) / 10)]
    else:
        return words[int((digit - 20) / 10)] + single_digit(int(dig[1]))


def triple_digit(digit):
    dig = str(digit)

    if dig[1] == '0' and dig[2] == '0':
        return single_digit(int(dig[0])) + 'hundred'
    elif dig[1] == '0':
        return single_digit(int(dig[0])) + 'hundredand' + single_digit(int(dig[2]))
    else:
        return single_digit(int(dig[0])) + 'hundredand' + double_digit(int(dig[1] + dig[2]))


if __name__ == '__main__':
    total = sum(len(map_number_to_words(i)) for i in range(1, 1000))
    print(total + len('onethousand'))
    # map_number_to_words(21)

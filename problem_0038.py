from problem_0032 import is_pandigital

if __name__ == '__main__':
    all_prods = []
    for i in range(9233, 9488, 1):
        prod = 100_002 * i
        if (len(str(prod)) == 9) and (set(list('123456789')) - set(str(prod)) == set()):
            all_prods.append(prod)
    print(max(all_prods))

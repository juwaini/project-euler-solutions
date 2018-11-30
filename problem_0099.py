import math

if __name__ == '__main__':
    with open('files/p099_base_exp.txt') as file:
        count = 0
        all_exp = []
        for line in file:
            vals = line.split(',')
            count += 1
            all_exp.append(
                int(vals[1]) * math.log(int(vals[0]))
            )
        print(all_exp.index(max(all_exp)) + 1)
        print(all_exp)


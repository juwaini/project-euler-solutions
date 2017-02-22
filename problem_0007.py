from problem_0003 import is_prime


def get_the_nth_prime(n):
    count = 1
    num = 1
    while count <= n:
        num += 1
        if is_prime(num):
            print('prime[%d] is %d' % (count, num))
            count += 1

if __name__ == '__main__':
    get_the_nth_prime(10001)
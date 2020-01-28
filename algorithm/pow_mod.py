# -*-coding:utf8-*-


# return a ^ i % n
def pow_mod(a, i, n):
    if i == 0:
        return 1 % n
    tmp = pow_mod(a, i >> 1, n)
    tmp = tmp * tmp % n
    if i & 1:
        tmp = tmp * a % n
    return tmp


if __name__ == '__main__':
    print(pow_mod(2, 10, 10000))

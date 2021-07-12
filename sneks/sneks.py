import sys


def d(v):
    return v << 1


def e(b, j):
    return 5 * f(b) - 7 ** j


def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    x = f(n >> 1)
    y = f(n // 2 + 1)
    return g(x, y, not n & 1)


def g(x, y, l):
    if l:
        return h(x, y)
    return x ** 2 + y ** 2


def h(x, y):
    return x * j(x, y)


def j(x, y):
    return 2 * y - x


def enc(litera, index):
    return d(e(litera, index))


if __name__ == '__main__':
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet += alphabet.upper()
    alphabet += "0123456789{\}_+-!@#$%^&*()`~;'"

    text = open("output.txt", "r").read().split()
    print(text)

    ans = ""
    for i in range(len(text)):
        for litera in alphabet:
            if(enc(ord(litera), i) == int(text[i])):
                ans += litera

    print(ans)

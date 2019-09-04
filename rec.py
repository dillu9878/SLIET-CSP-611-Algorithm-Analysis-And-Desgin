import time


def rec(n):
    if n == 1:
        return 1
    s = n * rec(n-1)
    return s


def rec1(n):
    if n == 1:
        return 1
    s = 0
    for i in range(n):
        s += rec1(n-1)
    return s


def rec2(n):
    if n == 1:
        return 1
    return


def rec3(n):
    if n == 1:
        return 1
    c = 10
    #c = 10**9
    #c = n
    return c + rec3(n-1)


def rec4(n):
    if n == 1:
        return 1
    return rec4(n-1) + rec4(n-1) + rec4(n-1) + rec4(n-1) + rec4(n-1) + rec4(n-1) + rec4(n-1) + rec4(n-1) + rec4(n-1) + rec4(n-1)


def rec5(n):
    if n == 1:
        return 1
    return 10*rec5(n-1)


if __name__ == '__main__':
    t1 = time.time()
    print(rec5(9))
    t2 = time.time()
    print(rec4(9))
    t3 = time.time()
    print(t2-t1, t3-t2)
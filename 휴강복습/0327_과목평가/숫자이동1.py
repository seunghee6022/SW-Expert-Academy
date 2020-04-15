import sys

sys.stdin = open('t.txt', 'r')

import copy


def move(n, k, li, result):
    global res, f0, f9
    f0, f9 = False, False

    if n == k:
        return

    for i in range(10):
        if abs(li[i]) < 10:
            if li[i] == 0:
                continue

            elif li[i] > 0:
                if i < 9:
                    result[i + 1].append(li[i])
                else:
                    result[i].append(li[i])
                    f9 = True
            elif li[i] < 0:
                if i > 0:
                    result[i - 1].append(li[i])
                else:
                    result[i].append(li[i])
                    f0 = True
        else:
            if i < 9:
                result[i + 1].append(abs(li[i]) // 2)
            if i == 9:
                result[i].append(abs(li[i]) // 2)
                f9 = True
            if i > 0:
                result[i - 1].append(-abs(li[i]) // 2)
            if i == 0:
                result[i].append(-abs(li[i]) // 2)
                f0 = True

    for i in range(10):
        if ((i == 0 and f0) or (i == 9 and f9)):
            if result[i] == []:
                result[i] = 0
            else:
                result[i] = -sum(result[i])
        else:
            if result[i] == []:
                result[i] = 0
            else:
                result[i] = sum(result[i])

    empty = [[] for _ in range(10)]
    res = copy.deepcopy(result)
    move(n + 1, k, result, empty)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = [int(x) for x in input().split()]
    result = [[] for _ in range(10)]
    res = [0] * 10

    move(0, N, li, result)

    print("#{} {}".format(tc, res))

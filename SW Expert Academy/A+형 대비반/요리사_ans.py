def f(n, k, a, b):
    global minV
    if n==k:
        diff = abs(taste(A, k) - taste(B, k))
        if minV > diff:
            minV = diff
    else:
        if a<k//2:
            A.append(n)
            f(n+1, k, a+1, b)
            A.pop()
        if b<k//2:
            B.append(n)
            f(n+1, k, a, b+1)
            B.pop()


def taste(food, k):
    s = 0
    for i in range(k//2):
        for j in range(i+1, k//2):
            s += synergy[food[i]][food[j]]
            s += synergy[food[j]][food[i]]
    return s

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = []
    B = []
    minV = 10000000000
    synergy = [list(map(int, input().split())) for _ in range(N)]
    f(0, N, 0, 0)
    print('#{} {}'.format(tc, minV))
def Permutation(n, k, Sum):
    global Min

    if Sum > Min :
        return

    if k == n:
        if Sum < Min: Min = Sum
        return

    else:
        for i in range(k, n):
            idx[i], idx[k] = idx[k], idx[i]
            Permutation(n, k + 1, Sum + data[k][idx[k]])
            idx[i], idx[k] = idx[k], idx[i]
import sys
sys.stdin = open('dummy.txt','r')


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    idx = list(range(N))
    data = [[int(x) for x in input().split()] for _ in range(N)]
    Min = 10000000000000000
    Permutation(N , 0 , 0)
    print("#{} {}".format(tc,Min))


import sys
sys.stdin= open("t.txt")

def printarr(arr):
    for i in range(N):
        print(arr[i])
    print()

# def Perm(n,k):
#     if n == k:
#         print(idx)
#
#     else :
#         for i in range(n,k):
#             idx[i],idx[n] = idx[n],idx[i]
#             Perm(n+1,k)
#             idx[i], idx[n] = idx[n], idx[i]

def f(n,k,s):
    global Max

    if s*100 <= Max: return

    elif n == k:
        if s*100 > Max : Max = s*100
        return

    for i in range(k):
        if not u[i]:
            u[i] = 1
            f(n+1,k,s*(pb[n][i]*0.01))
            u[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pb = [[int(x) for x in input().split()] for _ in range(N)]

    Max = 0
    u = [0]*N

    f(0, N, 1)
    print("#{} {:.6f}".format(tc,Max))
import sys
sys.stdin = open('dummy.txt','r')

def dfs(v):
    visited[v] = 1

    for w in range(N):
        if not visited[w]:
            dfs(w)


def Perm(n,k):
    if n==k:



    else :
        for i in range(k,n):
            arr[i], arr[k]= arr[k],arr[i]
            Perm(n,k+1)
            arr[i], arr[k]= arr[k],arr[i]





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [range(N)]
    visited= [0] * N
    customers = [int(x) for x in input().split()]


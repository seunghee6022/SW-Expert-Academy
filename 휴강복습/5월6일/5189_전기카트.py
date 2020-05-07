import sys
sys.stdin = open('t.txt','r')

#순열
def f(n,k,s,prev):
    global Min
    # print(n,s,v)
    if n == k-1 :
        s+=G[prev][0]
        if s < Min :
            Min = s
            s-=G[prev][0]
        return
    if s > Min :
        return
    else :
        for i in range(1,k):
            if not v[i]:
                if n < k-1 and i!=prev:
                    v[i] = 1
                    print(n, prev, i, s, v)
                    f(n+1,k,s+G[prev][i],i)
                    v[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    G = [[int(x) for x in input().split()] for _ in range(N)]
    v = [0]*N
    Min = 1000000000000
    f(0,N,0,0)
    print("#{} {}".format(tc,Min))
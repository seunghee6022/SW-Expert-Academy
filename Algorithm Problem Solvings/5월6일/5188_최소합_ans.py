import sys
sys.stdin = open('t.txt','r')

def Minsum(r,c,sum):
    global Min

    if r == N-1 and c == N-1:

        if Min > sum:
            Min = sum
        return
    #가지치기
    if sum > Min :
        return

    else:
        if r+1 < N :
            Minsum(r+1,c,sum+G[r+1][c])
        if c+1 < N :
            Minsum(r,c+1,sum+G[r][c+1])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    G = [[int(x) for x in input().split()] for _ in range(N)]
    Min = 10000000
    Minsum(0,0,G[0][0])
    print("#{} {}".format(tc,Min))



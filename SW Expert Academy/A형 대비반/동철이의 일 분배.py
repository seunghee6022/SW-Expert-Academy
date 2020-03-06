import sys
sys.stdin = open('dummy.txt','r')


def Perm(n,k,p):
    global Max, u

    if n == k :
        if Max < p*100 :
            Max = p*100
        return
    elif p*100 <= Max:
        return

    for i in range(n):
        if u[i]==0 :
            u[i] = 1
            Perm(n,k+1,p*P[i][k]/100)
            u[i] = 0



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    u = [0]*N
    Max = 0
    P= [list(map(int,input().split())) for _ in range(N)]
    Perm(N, 0, 1)
    print("#{} {:.6f}".format(tc, Max))
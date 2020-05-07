import sys
sys.stdin = open('t2.txt','r')

def perm(n,k, sum):
    global cnt
    if sum not in s :
        cnt+=1
        s.append(sum)

    if n==k :
        return
    else :
        arr[n] = 0
        perm(n+1,k,sum)
        arr[n] = 1
        perm(n+1,k,sum+score[n])




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    score = [int(x) for x in input().split()]
    v = [0]*N
    arr = [0]*N
    s = []
    cnt = 0
    perm(0,N,0)
    print(s)
    print("#{} {}".format(tc, cnt))
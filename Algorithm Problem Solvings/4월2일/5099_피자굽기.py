import sys
sys.stdin = open('t.txt','r')

T = int(input())
for tc in range(1,T+1):
    L,N = map(int,input().split())

    pizza = [int(x) for x in input().split()]
    oven = pizza[:L]
    loc = list(range(L))
    cur = L
    while cur != N:
        for i in range(L):
            oven[i]//= 2
            if oven[i] == 0 and cur <= N-1 :
                oven[i] = pizza[cur]
                loc[i] = cur
                cur += 1

    while (oven.count(0)+ oven.count(1)) < L :
        for i in range(L):
            oven[i]//=2

    for i in range(L-1,-1,-1):
        if oven[i] == 1 :
            print("#{} {}".format(tc,1+loc[i]))
            break





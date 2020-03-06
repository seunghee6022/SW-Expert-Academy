import sys
sys.stdin = open('dummy.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    H = [int(x) for x in input().split()]
    prox = 1000000

    for i in range(1<<N):
        Sum = 0
        flag = True
        for j in range(N):
            if i&(1<<j) and flag:
                Sum+=H[j]
                if Sum == B : prox == B; flag = False
                if Sum > prox : flag = False

        if B <= Sum < prox and flag :
            prox = Sum

    print("#{} {}".format(tc,prox-B))

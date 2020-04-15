import sys
sys.stdin = open('dummy.txt','r')

def f(n,a,b):
    global s_a,s_b, Min

    if a==N//2 and b==N//2:
        for i in A:
            for j in A :
                s_a += ing[i][j]
        for i in B:
            for j in B:
                s_b += ing[i][j]
        if Min > abs(s_a - s_b) : Min = abs(s_a - s_b)
        s_a, s_b = 0, 0

    else :
        if a <= (N//2-1):
            A.append(n)
            f(n+1,a+1,b)
            A.pop()

        if b <= (N // 2 - 1):
            B.append(n)
            f(n+1,a,b+1)
            B.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = [0]
    B = []
    s_a,s_b = 0, 0
    Min = 1000000000000
    ing = [list(map(int,input().split())) for _ in range(N)]

    f(1,1,0)

    print("#{} {}".format(tc,Min))



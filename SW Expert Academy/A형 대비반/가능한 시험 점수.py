import sys
sys.stdin = open('dummy.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int,input().split()))
    A = [1]+[0]*(sum(scores))

    S = [0]
    for score in scores :
        S.append(score)
        A[score] = 1
        for s in S[:-1]:
            if not A[s+ score]:
                S.append(s+score)
                A[s+score] = 1

    cnt = 0
    for i in range(len(A)):
        if A[i] : cnt +=1

    print("#{} {}".format(tc,cnt))

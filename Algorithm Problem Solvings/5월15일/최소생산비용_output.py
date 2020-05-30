import sys
sys.stdin = open('최소생산비용_input.txt','r')

def backtrack(result,selected,idx,N, numsum):
    global Min
    if numsum > Min:
        return

    if idx == N :
        if Min > numsum:
            Min = numsum
        return

    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            result[idx] = i
            backtrack(result,selected,idx+1,N,numsum+G[idx][i])
            selected[i] = 0
            numsum - G[idx][i]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    G = [[int(x) for x in input().split()] for _ in range(N)]
    Min = 1000000

    backtrack([0]*N, [0]*N, 0, N, 0)
    print("#{} {}".format(tc,Min))
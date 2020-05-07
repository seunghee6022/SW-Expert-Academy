def dfs(i,j,sum):
    global Min
    if i == N-1 and j == N-1 :
        if Min > sum :
            Min = sum
        return
    #가지치기
    if Min < sum:
        return
    #대각선 오른쪽으로 내려가면 되므로-> 아래, 오른쪽
    for dx, dy in [(1,0),(0,1)]:
        x, y = i+dx, j+dy
        if (0<=x<N and 0<=y<N):
            dfs(x,y,sum+G[x][y])



import sys
sys.stdin = open('t.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    G = [[int(x) for x in input().split()] for _ in range(N)]

    Min = 10000000
    dfs(0,0,G[0][0])
    print("#{} {}".format(tc,Min))
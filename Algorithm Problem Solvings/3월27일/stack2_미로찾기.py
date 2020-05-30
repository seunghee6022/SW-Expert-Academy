import sys
sys.stdin = open('t.txt','r')


def dfs(i,j):
    global result
    v[i][j] = 1

    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        x, y = i+dx, j+dy
        if not(0<=x<N and 0<=y<N): continue

        if G[x][y]==3: result = 1; return
        elif G[x][y]==0 and not v[x][y] :
            dfs(x,y)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    G = [[int(x) for x in input()] for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    
    result = 0

    for i in range(N-1,-1,-1):
        for j in range(N):
            if G[i][j] == 2:
                dfs(i,j)
                break


    print("#{} {}".format(tc,result))
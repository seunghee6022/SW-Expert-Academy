import sys
sys.stdin = open('dummy.txt','r')

def delta_bfs(s_x,s_y):
    global Max , cnt, val
    q = []
    visited = [[0]*N for _ in range(N)]
    q.append([s_x,s_y])
    while q :
        x, y = map(int,q.pop(0))
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            i , j = x+dy, y+dx
            if not (0 <=i< N and 0 <=j< N ) :
                continue
            if not visited[i][j] and data[i][j] == data[x][y]+1 :
                cnt += 1
                q.append([i,j])
                visited[i][j]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data= [[int(x) for x in input().split()] for _ in range(N)]

    Max, val ,x ,y = 0, 0, 0 ,0

    for i in range(N):
        for j in range(N):
            cnt = 1
            delta_bfs(i, j)
            if Max > cnt : continue

            elif Max == cnt and data[i][j] < val:
                val = data[i][j]

            elif Max < cnt :
                Max = cnt
                val = data[i][j]

    print("#{} {} {}".format(tc,val,Max))


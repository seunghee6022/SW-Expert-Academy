import sys
sys.stdin = open('dummy.txt','r')


def dfs(i,j,c,e):
    global Max
    if Max < e : Max = e

    v[i][j] = 1

    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        x, y = i+dx, j+dy
        if not (0<=x<N and 0<=y<N) :continue
        if not v[x][y] and hike[x][y] < hike[i][j]:
            dfs(x,y,c,e+1)
        elif not v[x][y] and c and hike[x][y]-K < hike[i][j]:
            org = hike[x][y]
            hike[x][y] -= 1
            dfs(x,y,c-1,e+1)
            hike[x][y] = org
    v[i][j] = 0

T = int(input())
for tc in range(1,T+1):
    N , K = map(int,input().split())
    hike = [[int(x) for x in input().split()] for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    Max = 0

    h = 0
    h_list = []
    for i in range(N):
        for j in range(N):
            if h < hike[i][j] :
                h = hike[i][j]
                h_list = [(i,j)]
            elif h == hike[i][j] :
                h_list.append((i,j))

    for idx in h_list :
        dfs(*idx,1,1)

    print("#{} {}".format(tc,Max))


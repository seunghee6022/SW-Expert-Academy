#bfs
import sys
sys.stdin = open('dummy.txt','r')
def printarr(arr):
    print("Start printarr")
    for i in range(N):
        print(arr[i])
    print()


def f_bfs(i,j,flag):
    if q :
        i, j = q.pop()
        for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:

            x, y = i+dx, j+dy


            if not (0<=x<N and 0<=y<N) : continue

            if flag :
                hike[x][y]-=K
                # print("hike[{}][{}] : {}".format(x,y,hike[x][y]))

            if not v[x][y] and hike[x][y]<hike[i][j] :
                print("hike[{}][{}] : {}".format(x, y, hike[x][y]))
                q.append((x,y))
                v[x][y] = v[i][j]+1
                # if v[x][y] > K : return
        flag = False
        f_bfs(x,y,flag)







T = int(input())
for tc in range(1, T + 1):
    N ,K = map(int,input().split())
    hike = [list(map(int, input().split())) for _ in range(N)]


    top_val = 0
    for i in range(N):
        if top_val < max(hike[i]): top_val = max(hike[i])

    top = []
    for i in range(N):
        for j in range(N):
            if hike[i][j] == top_val:
                top.append((i,j))

    for idx in top :
        q = [idx]
        v = [[0]*N for _ in range(N)]
        v[idx[0]][idx[1]] = 1
        f_bfs(*idx,True)
        printarr(v)


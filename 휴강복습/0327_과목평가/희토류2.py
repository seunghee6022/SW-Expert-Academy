import sys
sys.stdin = open('t2.txt','r')

def bfs(val):
    global area,cnt,Mcnt,Rarea
    if len(q)==0:
        if Mcnt < cnt :
            Mcnt = cnt
            Rarea = area
        elif Mcnt==cnt and Rarea>area:
            Rarea = area
        return

    else :
        i,j = map(int,q.pop(0))
        for dx,dy in [(0,1),(-1,0),(0,-1),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            x,y = i+dx,j+dy

            if not (0<=x<N and 0<=y<N): continue
            if not v[x][y] and G[x][y]==val:
                v[x][y]=1
                area+=1
                cnt+=val
                q.append((x,y))
        bfs(val)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    G = [[int(x) for x in input().split()] for _ in range(N)]

    v = [[0]*N for _ in range(N)]
    Rarea,Mcnt = 0,0

    for i in range(N):
        for j in range(N):
            if not v[i][j] and G[i][j]:
                area, cnt = 1, G[i][j]
                v[i][j] = 1
                q = [(i,j)]
                bfs(G[i][j])
    print("#{} {} {}".format(tc,Mcnt,Rarea))
import sys
sys.stdin = open('t.txt','r')

def sand():
    global cnt, flag
    if not q :
        cnt+=1

    i,j = map(int,q.pop(0))
    sand_cnt = 0
    if G[i][j].isdecimal(): G[i][j]=int(G[i][j])
    for dx,dy in [(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]:
        x,y = i+dx,j+dy

        if not(0<=x<N and 0<=y<M): continue

        if G[x][y]=='.' : sand_cnt+=1
        elif not v[x][y] and G[x][y].isdecimal():
            q.append((x,y))
            v[x][y] = 1

    if G[i][j]<= sand_cnt :
        G[i][j]-=1
        if G[i][j] == 0 : G[i][j]='.'
        flag = False

    sand()



T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    G = [[x for x in input()] for _ in range(N)]

    cnt= 0

    while True :
        v = [[0] * M for _ in range(N)]
        flag = True
        q = [(0,0)]
        v[0][0] = 1
        sand()
        if flag: break

    print("#{} {}".format(tc,cnt))

import sys
sys.stdin = open('t.txt','r')

def printarr(arr):
    for i in range(R):
        print(arr[i])
    print()

from collections import deque

def bfs(wolf, sheep):
    global Wolf, Sheep
    while q :
        i,j = map(int,q.popleft())
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            x, y = i+dx, j+dy
            if (0<=x<R and 0<=y<C) and not v[x][y]:
                if yard[x][y] == '#' :
                    v[x][y] = 1
                else :
                    v[x][y] = 2
                    q.append((x,y))
                    if yard[x][y] == 'v' : wolf+=1
                    elif yard[x][y] == 'o' : sheep+=1

    if wolf >= sheep : Wolf+=wolf
    else : Sheep+=sheep


T = int(input())
for tc in range(1,T+1):
    R,C = map(int,input().split())
    yard = [[x for x in input()] for _ in range(R)]
    Wolf, Sheep = 0, 0
    v = [[0]*C for _ in range(R)]

    for i in range(1,R-1):
        for j in range(1,C-1):
            if not v[i][j]:
                q = deque()
                q.append((i,j))
                v[i][j] = 2
                if yard[i][j] == 'v': bfs(1,0)
                elif yard[i][j] == 'o' : bfs(0,1)
                else : bfs(0,0)


    print(Sheep, Wolf)


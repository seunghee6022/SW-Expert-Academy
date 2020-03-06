import sys
sys.stdin = open('dummy.txt','r')

def delta_bfs(x,y):
    visited = [[0]*M for _ in range(N)]
    q = []
    q.append((x,y))
    visited[x][y] = 1

    while q:
        v = q.pop(0)
        for dx_j, dy_i in [(0,1),(0,-1),(1,0),(-1,0)]:
            i, j = x + dy_i, y + dx_j

            if not ( 0<=i<N and 0<=j<M ) : continue

            if G[i][j] and not visited[i][j]:





N, M = map(int, input().split())
G = [[int(x) for x in input()] for _ in range(N)]
print(G)

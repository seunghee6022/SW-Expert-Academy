import sys
sys.stdin = open('dummy.txt','r')
#최단거리 - BFS
#최단거리 = 시작점에서부터 도착점까지의 level 차
#distance는 level을 의미한다. 따라서 d[x][y]가 나오자마자 break를 해도 이미 최단거리가 구해졌기 때문에 괜춘.

def delta_bfs(x,y):
    global Min
    q = [(x,y)]
    # start -> v 까지 최단 경로의 길이
    d = [[0]*M for _ in range(N)]
    d[0][0] = 1
    visited = [(x,y)]
    while q:
        x,y = map(int, q.pop(0))

        if x == N - 1 and y == M - 1:
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i, j = x + dy, y + dx
            if not (0 <= i < N and 0 <= j < M):
                continue
            elif G[i][j] and (i,j) not in visited:
                visited.append((i,j))
                d[i][j] = d[x][y] + 1
                q.append((i,j))
    return d[x][y]

N, M = map(int,input().split())
G = [[int(x) for x in input()] for _ in range(N)]
print(delta_bfs(0,0))



import sys
sys.stdin = open('색종이붙이기.txt', 'r')

from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    G = [[x for x in input()] for _ in range(N)]
    q = deque()
    v = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if G[i][j] == '.':
                G[i][j] = 0
                v[i][j] = 1
                q.append((i,j))
            else : G[i][j] = int(G[i][j])

    while q:
        i, j = map(int, q.popleft())
        for dx, dy in [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]:
            x, y = i + dx, j + dy
            if (0 <= x < N and 0 <= y < M):
                if 2 <= G[x][y] < 9:
                    G[x][y] -= 1
                elif G[x][y] == 1 and not v[x][y]:
                    G[x][y] = 0
                    v[x][y] = v[i][j]+1
                    if v[x][y] > cnt : cnt = v[x][y]
                    q.append((x, y))



    print("#{} {}".format(tc,cnt-1))

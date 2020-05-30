import sys
sys.stdin = open('t.txt','r')

def L_cnt(arr):
    c = 0
    for i in range(N):
        for j in range(M):
            if 0 < arr[i][j] <= L:
                c += 1
    return c


def bfs():
    if q:
        i, j = map(int, q.pop(0))

        for dir in pipes[tunnel[i][j]]:
            x, y = i + delta[dir][0], j + delta[dir][1]
            if (0 <= x < N and 0 <= y < M) and not v[x][y] and 3 - dir in pipes[tunnel[x][y]]:
                v[x][y] = v[i][j] + 1
                q.append((x, y))
        bfs()


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    # 상:0 , 우:1, 좌:2, 하:3
    delta = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    pipes = [[], [0, 1, 2, 3], [0, 3], [1, 2], [0, 1], [1, 3], [2, 3], [0, 2]]
    v = [[0] * M for _ in range(N)]
    v[R][C] = 1
    q = [(R, C)]
    bfs()
    print("#{} {}".format(tc, L_cnt(v)))
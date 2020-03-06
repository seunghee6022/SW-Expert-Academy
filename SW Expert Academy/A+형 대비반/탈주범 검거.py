import sys
sys.stdin = open('dummy.txt','r')


def f(N, M, R, C, L):
    q = [(R,C)]
    v = [[0] * M for _ in range(N)]
    v[R][C] = 1
    pos = [0] * (L + 1)

    while q:
        i, j = q.pop(0)
        pos[v[i][j]] += 1
        if v[i][j] < L :
            for x in pipes[tunnel[i][j]]:
                ni, nj = i + di[x], j +dj[x]

                if 0<=ni<N and 0<=nj<M and tunnel[ni][nj] and not v[ni][nj] and (x+2)%4 in pipes[tunnel[ni][nj]] :
                    v[ni][nj] = v[i][j]+1
                    q.append((ni,nj))

    return sum(pos)

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [[int(x) for x in input().split()] for _ in range(N)]
    pipes = [[], [0, 1, 2, 3], [1,3], [0,2],[0, 3], [0,1], [1, 2], [2,3]]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    count = 0
    r = f(N,M,R,C,L)
    print("#{} {}".format(tc, r))

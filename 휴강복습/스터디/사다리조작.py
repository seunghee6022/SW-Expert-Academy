import sys
sys.stdin = open('t.txt', 'r')

def dfs(i,j,b_len):
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        x, y = i+dx, j+dy
        if not (0 <= x < N and 0 <= y < M) or G[x][y] == 1:
            continue

        elif not G[x][y] and not v[x][y]:
            #가로일 때 == 7
            if (dx,dy) in [(0,1),(0,-1)]:
                dir = 7
                
            #세로일 때 == 8
            else : dir = 8
            d, cnt = 0, 0
            xx, yy = x+(dx*d), y+(dy*d)
            while (0 <= xx < N and 0 <= yy < M) and v[xx][yy] != dir :
                cnt += 1
                v[xx][yy] = dir
                if G[xx][yy] == 1 :
                    dfs(xx, yy, b_len+cnt )
                    break
                d += 1
            v[xx][yy] = 0   
            
'''
### 이미 연결된 섬끼리 다리를 다시 안만들기 위한 중복 방지 방법 처리
처음에 섬을 돌고 넘버링을 한다.
섬 방문 배열을 만든다. 1사이즈 크게
차후에 배열에 돌았던 섬의 인덱스에 1처리한다.
다리 길이 1개 일 때 예외 처리도 아직 안핢.
'''

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    G = [[int(x) for x in input().split()] for _ in range(N)]
    v = [[0]*M for _ in range(N)]

    for i in range(N):
        print(G[i])
    print()

    for i in range(N):
        for j in range(M):
            if G[i][j] == 1 :
                dfs(i,j,0)
                print()
                break
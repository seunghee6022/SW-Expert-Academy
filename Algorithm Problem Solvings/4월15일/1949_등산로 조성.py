import sys
sys.stdin = open('등산로.txt','r')


def printarr(arr):
    for i in range(N):
        print(arr[i])
    print()

from collections import deque
import copy
def dfs(i,j):
    global long, K, k_cnt
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        x, y = i+dx, j+dy
        if (0<=x<N and 0<=y<N) and not v[x][y]:
            # 등산로 안깎아도 작을 때
            if G[x][y] < G[i][j] :
                v[x][y] = v[i][j]+1
                if v[x][y] > long:
                    long = v[x][y]
                dfs(x,y)

            # 더 높아서 등산로 깎으면 갈 수 있을 때
            elif k_cnt==1 and G[x][y]-K < G[i][j] :
                k_cnt = 0
                v[x][y] = v[i][j]+1
                if v[x][y] > long :
                    long = v[x][y]
                original = G[x][y]
                k = K
                while G[x][y] >= G[i][j] and k >= 0:
                    k-=1
                    G[x][y] -= 1
                dfs(x,y)
                k_cnt = 1
                G[x][y] = original
            v[x][y] = 0

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    original_G = []
    Max = 0
    top = 0
    #최고점의 위치
    top_loc = []
    for i in range(N):
        temp = [int(x) for x in input().split()]
        original_G.append(temp)
        for j in range(N):
            if temp[j] > top :
                top = temp[j]
                top_loc = [(i, j)]
            elif temp[j] == top :
                top_loc.append((i,j))

    q = deque()
    for t in top_loc :
        i,j = map(int,t)
        v = [[0]*N for _ in range(N)]
        v[i][j] = 1
        G = copy.deepcopy(original_G)
        long = 0
        k_cnt = 1
        dfs(i,j)

        if Max < long :
            Max = long
    print("#{} {}".format(tc,Max))





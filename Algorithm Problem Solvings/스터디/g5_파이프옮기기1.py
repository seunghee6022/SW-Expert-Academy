import sys
sys.stdin = open('파이프옮기기1.txt','r')
'''
항상 (0,0),(0,1)에 파이프 있고, 직선, 오른아래대각선, 수직으로만 파이프 연결해서 이동 가능
0아닌 곳 지나갈 수 없다.
N,N으로 가는 방법의 수
파이프가 가로일 때 -> 오른족, 대각선
세로 -> 아래, 대각선
대각선 -> 아래, 오른, 대각선

'''
def dfs(i, j, dir):
    global result
    print(i,j)
    # 오른, 아래, 대각
    dx = [0,1,1]
    dy = [1,0,1]
    # 오른
    if dir == 0 :
        dir_range = [0,2]
    # 아래
    elif dir == 1 :
        dir_range = [1,2]
    # 대각선
    else:
        dir_range = [0, 1, 2]


    for dir in dir_range:
        x, y = i+dx[dir], j+dy[dir]
        if 0<=x<N and 0<=y<N :
            if (dir == 0 or dir == 1) and not G[x][y]:
                if x == N - 1 and y == N - 1:
                    result += 1
                    printarr(G)
                    return
                G[x][y] = 3
                dfs(x, y, dir)
                G[x][y] = 0

            elif dir == 2 and not G[x][y] and not G[x-1][y] and not G[x][y-1]:
                if x == N - 1 and y == N - 1:
                    result += 1
                    printarr(G)
                    return
                G[x][y] = 3
                dfs(x, y, dir)
                G[x][y] = 0


def printarr(arr):
    for i in range(N):
        print(arr[i])
    print()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    G = [[int(x) for x in input().split()] for _ in range(N)]
    # G[0][0] = 3
    # G[0][1] = 3
    result = 0
    # dir : 오른0, 아래1, 대각2
    dfs(0,1,0)
    print("#{} {}".format(tc,result))



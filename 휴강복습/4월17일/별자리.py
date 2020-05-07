import sys
sys.stdin = open("input.txt",'r')


def dfs(i,j):
    # 기준 점을 중심으로 주변에 별이 있는지 8방향으로 검사
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
        x, y = i+dx, j+dy
        if (0<=x<10 and 0<=y<10):
            # 만약 방문하지 않은 별이 있다면 다음 dfs로
            if not v[x][y] and G[x][y]:
                v[x][y] = 1
                dfs(x,y)

T = int(input())
for tc in range(1,T+1):
    G  = [[int(x) for x in input().split()] for _ in range(10)]
    v = [[0]*10 for _ in range(10)]
    cnt = 0
    q = []

    for i in range(10):
        for j in range(10):
            # 맵에서 방문하지 않았고 별이 있다면 dfs의 시작점으로
            if G[i][j] and not v[i][j] :
                v[i][j] = 1
                # dfs의 횟수가 별자리 그룹의 개수
                cnt +=1
                dfs(i,j)

    print("#{} {}".format(tc,cnt))
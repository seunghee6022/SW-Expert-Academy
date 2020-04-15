import sys
sys.stdin= open("t.txt")

def f(s_x,s_y):
    global Max, val

    cnt = 1
    v[s_x][s_y] = 1
    visit[s_x][s_y] = 1
    q=[(s_x,s_y)]

    while q:
        i, j = map(int,q.pop())
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            x,y = i+dx,j+dy
            if (0<=x<N and 0<=y<N) and not v[x][y] and room[x][y] == room[i][j]+1:
                cnt+=1
                v[x][y] = 1
                visit[x][y] = 1
                q.append((x,y))


    if Max < cnt :
        # print("Max<cnt",x,y,room[s_x][s_y])
        Max = cnt
        val = room[s_x][s_y]
        # print(val)
    elif Max == cnt and val > room[s_x][s_y]: val = room[s_x][s_y]

def printarr(arr):
    for i in range(N):
        print(arr[i])
    print()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [[int(x) for x in input().split()] for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    Max = 0
    val = 0

    for i in range(N):
        for j in range(N):
            # print("val,Max,visit",val,Max)
            # printarr(visit)
            # v = [[0] * N for _ in range(N)]
            if not visit[i][j]:
                # print("not visited",i,j)
                v = [[0] * N for _ in range(N)]
                # printarr(v)
                f(i,j)
                # print("v",val,Max)
                # printarr(v)

    print("#{} {} {}".format(tc,val,Max))
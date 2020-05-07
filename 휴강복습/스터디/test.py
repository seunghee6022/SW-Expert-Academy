import sys
sys.stdin = open('t.txt','r')
'''
<1초동안 미세먼지의 확산 계산하기>
1. matrix를 받아올 때 청소기의 위치를 저장.
2. 배열에서 먼지가 있는 위치만 저장
3. 먼지 있는곳 방문. 
배열 만듬. [a:확산시키고 남은 미세먼지, b:더해줄 확산된 미세먼지]
3-1.만약 5보다 크다면 
    5한 몫을 주변4방향 중 범위 안이면 나눠주면서 나눠준 횟수 카운트, 나눠준값 배열에 저장.[확산시키고 남은 미세먼지, 더해줄 확산된 미세먼지]
3-2 작다면 , 나눠준 카운트 0하고 pass =>  [원래 미세먼지 양 그대로, 더해줄 확산된 미세먼지]
4. 배열을 다시 돌면서 a+b해서 [a+b, 0] 으로 만들어주고 a+b가 5이상이면 다음 bfs위한 q에 저장한다.

<1초동안 진공청소기 돌리고 난 후>
1. 위 -진공청소기 열2칸 자리중 위쪽 좌표를 시작
    1-1. 그 좌표를 시작으로 반시계로 배열의 값을 한칸씩 밀어서 바꾼다.
2. 아래 - 아래 좌표를 시작
    1-2 시계방향 ...
'''



def spreading_dust(dust_list):
    global up_x,up_y,down_y,down_x
    #다음 미세먼지 리스트
    new_dust_list = []
    spread_cnt = 0
    for dust_loc in dust_list:
        i,j = map(int,dust_loc)
        dust = G[i][j][0]
        # 미세먼지가 5보다 작으면 건너뛰기
        if dust < 5: continue
        # 5보다 크면 주변에 확산시키기
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            x, y = i+dx, j+dy
            if ( 0 <= x < R and 0 <= y < C ) and G[x][y][0] != -1:
                #미세먼지 확산
                spread_cnt += 1
                if [x,y] not in dust_list :
                    G[x][y][0] += dust//5
                    if G[x][y][0] >= 5 and [x,y] not in new_dust_list and x not in [0, R-1, up_x, down_x] and y not in [0, C-1, up_y, down_y] :
                        new_dust_list.append([x,y])
                else :
                    G[x][y][1] += dust//5

        # 확산되고 남은 기존의 먼지
        G[i][j][0] -= (dust//5)*spread_cnt
        spread_cnt = 0

    #미세먼지 합산
    while dust_list:
        i, j = map(int,dust_list.pop())
        spread_dust = G[i][j][1]
        if spread_dust :
            G[i][j][0] += spread_dust
            G[i][j][1] = 0

        if G[i][j][0] >= 5 and [i,j] not in new_dust_list and i not in [0, R-1, up_x, down_x] and j not in [0, C-1, up_y, down_y]:
            new_dust_list.append([i,j])

    return new_dust_list


def air_cleaner(up_x, up_y,down_x,down_y, new_dust_list):
    new_G = [[0,0]*C for _ in range(R)]
    new_G[up_x][up_y] = [-1, 0]
    new_G[down_x][down_y] = [-1, 0]
    #위쪽부터(반시계)
    #왼쪽아래->오른아래

    for dy in range(up_y+1,C-1):
        new_G[up_x][dy+1] = G[up_x][dy]
        if new_G[up_x][dy+1] >= 5 :
            new_dust_list.append([up_x,dy+1])


    #오른아래->오른위
    for dx in reversed(range(1,up_x)):
        new_G[dx-1][C-1][0] = G[dx][C-1][0]
        if new_G[dx-1][C-1][0] >= 5 :
            new_dust_list.append([dx-1,C-1])


    #오른위->왼위
    for dy in reversed(range(C-1)):
        cur = G[0][dy][0]
        G[0][dy][0] = prev
        if prev >= 5 :
            new_dust_list.append([0,dy])
        prev = cur

    #왼위->왼아래
    for dx in range(1,up_x):
        cur = G[dx][0][0]
        G[dx][0][0] = prev
        if prev >= 5 :
            new_dust_list.append([dx,0])
        prev = cur


    #아래쪽(시계)
    #왼쪽위->오른위
    prev,cur = 0, 0
    for dy in range(down_y+1,C):
        cur = G[down_x][dy][0]
        G[down_x][dy][0] = prev
        if prev >= 5 :
            new_dust_list.append([down_x,dy])
        prev = cur

    #오른위->오른아래
    for dx in range(down_x+1,R):
        cur = G[dx][C-1][0]
        G[dx][C-1][0] = prev
        if prev >= 5 :
            new_dust_list.append([dx,C-1])
        prev = cur

    #오른아래 -> 왼아래
    for dy in reversed(range(C-1)):
        cur = G[R-1][dy][0]
        G[R-1][dy][0] = prev
        if prev >= 5 :
            new_dust_list.append([R-1,dy])
        prev = cur

    #왼아래->왼위
    for dx in reversed(range(down_x+1, R-1)):
        cur = G[dx][0][0]
        G[dx][0][0] = prev
        if prev >= 5 :
            new_dust_list.append([dx,0])
        prev = cur

    return new_dust_list

# def printarr(arr):
#     for i in range(R):
#         print(arr[i])
#     print()

def cal_sum(arr):
    Sum = 0
    for i in range(R):
        for j in range(C):
            Sum+=arr[i][j][0]
    return Sum

R, C, T = map(int,input().split())
G = [[] for _ in range(R)]
dust_list = []
m_loc = []
for i in range(R):
    temp = list(map(int,input().split()))
    for j in range(C) :
        G[i].append([temp[j],0])
        if temp[j] == -1 :
            m_loc.append([i,j])
        elif temp[j] :
            dust_list.append([i,j])

down_x,down_y = map(int,m_loc.pop())
up_x, up_y = map(int,m_loc.pop())
for _ in range(T):
    new_dust_list = (spreading_dust(dust_list))
    dust_list = air_cleaner(up_x,up_y,down_x,down_y,new_dust_list)

Sum = cal_sum(G)+2
print(Sum)
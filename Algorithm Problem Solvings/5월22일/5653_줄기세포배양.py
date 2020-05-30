import sys
sys.stdin = open('줄기세포배양.txt','r')
# K시간 후 살아있는 줄기 세포(비활성 상태 + 활성 상태)의 총 개수를 구하는 프로그램

# 현재시간, 추가된 시간 - > 현재시간 - 추가된시간 <= 수명 : 살아있는 줄기세포이다.

def search_alive(s,e,plate):
    v = [[0] * 1000 for _ in range(1000)]
    if plate[s][e] != 0:
        v[s][e] = 1




from collections import deque
def product(s,e,life,add_time,cur_time):
    #left는 젤 직은거, right는 젤 큰거 search range
    x_left, x_right, y_left, y_right = 500, 500, 500, 500
    alive_cnt = 0
    q = deque()
    q.append((s,e,plate[s][e][0],plate[s][e][1]))

    while q:
        i, j, life, add_time = q.popleft()
        if i < x_left : x_left = i
        elif i > x_right : x_right = i
        if j < y_left : y_left = j
        elif j > y_right : y_right = j

        if cur_time - add_time <= life :
            alive_cnt+=1
            print("alive",i,j)
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            x, y = i+dx, j+dy
            # 만약 활성화상태면 확장
            if (0<=x<1000 and 0<=y<1000) and (cur_time-add_time)//life == 1 :
                # 이게 빈 공간인지 확인해야함 -> 빈공간이면 수명 큰걸로 갱신
                # 1. 빈공간인지는 0이거나
                if not plate[x][y]:
                    plate[x][y] = [life, cur_time]
                # 2. plate[x][y][1](=add_time)이 cur_time이면 !!!
                elif plate[x][y][1] == cur_time and plate[x][y][0] < life:
                    plate[x][y][0] = life

    return alive_cnt


T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    plate = [[0]*1000 for _ in range(1000)]
    alive=[]
    i_start = (1000-N)//2
    j_start = (1000-M)//2


    for i in range(N) :
        temp = list(map(int,input().split()))
        for j in range(M):
            #수명, 추가된 시간 넣기
            if temp[j]:
                plate[i+i_start][j+j_start] = [temp[j],0]
                # 살아있는 세포 추가 - i,j,life,add_time
                alive.append([i,j,temp[j],0])


    # bfs할 때마다 cur_time ++
    for cur_time in range(K):
        # 범위를
        product(i_start, j_start,  plate[i_start][j_start][0] ,  plate[i_start][j_start][1] , cur_time)




# <문제 설명>
# 최소 시간으로 한 방에서 만나야함(같은 문 동시 통과는 인정 x, 반드시 만날 수 있다.)
# 1. 출발할 수 있는 방 3곳
# 2. 3곳 중 2곳 골라서 시작
#
# 숫자 1: 들어갈 수 x, 0: 들어갈 수 o, 2: 출발지로 가능한 방
# 이동시간 최소 1분. 1분 후 반드시 이동해야하는 것 x
# ------------------------------------------------------------------------
# <Pesudo Code>

#시작점 3개 중 2개 고르는 순열
def perm(k):
    global v
    if k == 2:
        print(p)
        # p[0]가 인덱스인 start의 원소 : 시작점1
        i1 = start[p[0]][0]
        j1 = start[p[0]][1]
        # p[1]가 인덱스인 start의 원소 : 시작점2
        i2 = start[p[1]][0]
        j2 = start[p[1]][1]
        print(i1,j1,i2,j2,v[i1][j1])
        # 두 시작점에서 출발
        v = [[0] * N for _ in range(N)]
        v[i1][j1] = 1
        v[i2][j2] = 2
        running(i1,j1,i2,j2,0)
        return

    else:
        for i in range(3):
            # 만약 방문 안했다면
            if not visit[i]:
                visit[i] = 1
                p[k] = i
                perm(k+1)
                visit[i] = 0

# 두 시작점에 대해 상하좌우 4방향 + 머물러있을지 결정하는 함수
def running(i1,j1,i2,j2,t):
    global Min

    # 만약 두 점이 같은 시간대에 만나면
    # v[i1][j1]==[1,2]을 통해 통과x, 같은 방에서 만나도록
    if i1==i2 and j1==j2 :
        # 최소값을 비교
        if Min > t :
            Min = t
        return

    else:
        #시작점 1에 대해 상, 하, 좌, 우, 머무르기를 dx1,dy1을 시작점1의 좌표에 더해주기
        for dx1, dy1 in [(-1,0),(1,0),(0,-1),(0,1),(0,0)]:
            # 시작점 1의 좌표가 벗어나거나 들어갈 수 없는 방이면 continue
            if i1+dx1 < 0 or i1+dx1 >= N or j1+dy1 < 0 or j1+dy1 >= N or A[i1+dx1][j1+dy1]!=0 or v[i1+dx1][j1+dy1]==1: continue
            #시작점 2에 대해 상, 하, 좌, 우, 머무르기를 dx2,dy2을 시작점2의 좌표에 더해주기
            for dx2, dy2 in [(-1,0),(1,0),(0,-1),(0,1),(0,0)]:
                # 시작점 1과 2에 따른 결과를 좌표에 반영해주고, 시작점 둘의 시간을 각각 1씩 늘린다.
                # 시작점 1의 좌표가 벗어나거나 들어갈 수 없는 방이거나 이미 방문했으면 continue
                if i2+dx2 < 0 or i2+dx2 >= N or j2+dy2 < 0 or j2+dy2 >= N or A[i2+dx2][j2+dy2]!=0 or v[i2+dx2][j2+dy2]==2: continue
                # 각 좌표와 흐른 시간을
                v[i1+dx1][j1+dy1] = 1
                v[i2+dx2][j2+dy2] = 2
                running(i1+dx1, j1+dy1, i2+dx2, j2+dy2, t+1)
                v[i1 + dx1][j1 + dy1] = 0
                v[i2 + dx2][j2 + dy2] = 0

# ---------------입력데이터 저장하는 부분-------------------
import sys
sys.stdin = open('dummy.txt','r')
T = int(input())
for tc in range(1,T+1):
    ans = 0
    N =int(input())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    #배열 A 에서 시작점 찾기.
    start = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == 2:
                # 시작점 리스트에 시작점 x,y 좌표 추가
                start.append([i,j])

    #최소값
    Min = 1000

    # running함수용 방문행렬 v
    v = [[0]*N for _ in range(N)]
    # perm함수용 방문리스트
    visit = [0]*3
    p = [0] * 2
    # 시작점 2개를 선택하고, running함수를 실행하여 최소값을 찾음.
    perm(0)

    # 최소값 출력
    print("최소시간:",Min)
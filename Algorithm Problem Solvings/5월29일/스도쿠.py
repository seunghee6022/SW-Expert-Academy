import sys
sys.stdin = open('스도쿠.txt','r')

def check(i, j, num):
    global ans

    #만약 숫자가 이미 들어있으면 return
    if G[i][j] :
        return -1

    # 새 숫자를 스도쿠 판에 넣어줌
    G[i][j] = num

    # 1. 행을 검사
    # 1~9숫자 중복을 검사할 배열
    line = [0]*10
    for jj in range(9):
        # 만약 0이면 continue
        if G[i][jj] == 0: continue
        # 중복된 숫자 없으면 1~9자리에 1씩 더함
        if not line[G[i][jj]]:
            line[G[i][jj]] += 1
        # 만약 1~9사이의 중복된 숫자가 있으면 False를 return
        else:
            return -1

    # 2. 열을 검사
    # 1~9숫자 중복을 검사할 배열
    line = [0]*10
    for ii in range(9):
        # 만약 0이면 continue
        if G[ii][j] == 0: continue
        # 중복된 숫자 없으면 1~9자리에 1씩 더함
        if not line[G[ii][j]]:
            line[G[ii][j]] += 1
        # 만약 1~9사이의 중복된 숫자가 있으면 False를 return
        else:
            return -1

    # 3. 그 좌표가 있는 3*3 행렬 검사
    # 범위를 잡기위해 행,렬의 시작범위 정함
    # 좌표를 3으로 나눈 몫에서 3을 곱하면 시작범위
    start_i = (i//3)*3
    start_j = (j//3)*3
    # 1~9숫자 중복을 검사할 배열
    line = [0] * 10
    for x in range(start_i,start_i+3):
        for y in range(start_j,start_j+3):
            # 만약 0이면 continue
            if G[x][y] == 0: continue
            # 중복된 숫자 없으면 1~9자리에 1씩 더함
            if not line[G[x][y]]:
                line[G[x][y]] += 1
            # 만약 1~9사이의 중복된 숫자가 있으면 False를 return
            else:
                return -1

    # 만약 1~3 모두 만족한다면 스도쿠 문제 없음
    ans+=1

T = int(input())
for tc in range(1,T+1):
    ans = 0
    N = int(input())
    G  = [[int(x) for x in input().split()] for _ in range(9)]

    cords = []
    for i in range(N):
        cords.append(list(map(int,input().split())))

    # 만약 중간에 스도쿠 실패하면 바로 중단.
    # flag로 판단
    flag = True
    for cord in cords :
        if flag != -1 :
            flag = check(*cord)
        else:
            break
    print("#{} {}".format(tc,ans))

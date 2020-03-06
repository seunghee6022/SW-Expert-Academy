import sys
sys.stdin = open( '2048.txt','r' )

'''
방향에따라 for문 이용해서 game[i]의 위 아래면 i를 바꾸고 왼 / 오른쪽이면 game[:][j]이용.

만약에 같은 숫자가 마주치면 방향에 따라서 숫자를 합치고2 ** i 합쳐지기 전 위치 값은 0으로 해준다.

0제외한 숫자만 모아서 리스트 만든 뒤에 계산하면 pop해서 game리스트에 insert하자

방향 따라서 배열 각도만 돌리자(사실계산 방향은 하나인데, 배열만 돌려서 방향조절계산가능)
'''

def turn_arr(N, game, direction):
    arr = [[0] * N for _ in range(N)]
    if direction == 'right' : arr = game
    #좌우 반전
    if direction == 'left':
        for i in range(N):
            for j in range(N):
                arr[i][j] = game[i][-j - 1]
    # 90도 회전
    if direction == 'up':
        for i in range(N):
            for j in range(N):
                arr[j][i] = game[-i-1][j]
    # -90도 회전
    if direction == 'down':
        for i in range(N):
            for j in range(N):
                arr[j][i] = game[i][-j-1]
    return arr

def cal_right(N,arr):
    for i in range(N):
        # cal은 각 행의 계산할 값을 담은 리스트(계산 전)
        cal = []
        for j in range(N):
            if arr[i][j] != 0:
                cal.append(arr[i][j])
            else:
                continue
            # 계산한 값들 있는 리스트
        add =[]
        ii = -1
        if len(cal) == 1 : add = cal
        while ii > -len(cal):
            if cal[ii] != cal[ii-1] :
                add.append(cal[ii])
                ii-=1
            else :
                add.append(cal[ii]+cal[ii-1])
                ii-=2

            if -ii == len(cal) :
                add.append(cal[ii])
                break
        #     print("current add : {}".format(add))
        # print("i: {} , add : {}".format(i,add))
        # print("arr : {}".format(arr))
        #add가 완성되었으므로 arr에서 앞부분은 0으로 나머지는 add결과로 채우기.
        add.reverse()
        arr[i] = [0]*(N-len(add))+add

    return arr



T = int(input())
for tc in range(1, T + 1):
    n, direction = input().split()
    N = int(n)
    game = [0] * int(N)
    for i in range(N):
        game[i] = list(map(int, input().split()))


    arr = turn_arr(N, game, direction)
    arr = cal_right(N, arr)
    if direction == 'up':
        arr = turn_arr(N, arr, 'down')
    if direction == 'down':
        arr = turn_arr(N, arr, 'up')
    if direction == 'left':
        arr = turn_arr(N, arr, 'left')

    #final arr
    print("#{}".format(tc))
    for i in range(N):
        print(*arr[i])




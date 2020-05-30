'''
<감시>
type이
0:상, 1:하, 2:좌, 3:우 1,2,3,4,5인지에 따라 타입별로 비출 각도의 리스트를 만들기.
cctv마다 비출 방향의 순열리스트를 만들어 그 순서대로 모든 경우의 수 해보고 최소값 구하기.
* cctv번호가 큰 숫자부터 계산하기 -> 그래야 나중에 남는 0수가 적으니까 계산이 빨라짐
* 5는 무조건 4방향이므로 늘 계산이 동일 ->그래서 맨 먼저 시작하고 난 매트릭스로 나머지 타입에 대해 계산.

cctv타입별 각도리스트
1 = [[0],[1],[2],[3]]
2 = [[0,1],[2,3]]
3 = [[0,2],[0,3],[1,2],[1,3]]
4 = [[0,1,2],[0,1,3],[0,2,3],[1,2,3]]

가지치기
type 5부터 해서 만약 남은 사각지대 수가 0이면 더 하지 않고 return
'''

def right(i, j, G):
    cnt = 0
    if i == N - 1: return cnt
    for x in range(i + 1, N):
        if G[x][j] == 6:
            return cnt
        elif G[x][j] == 0:
            G[x][j] = 7
            cnt += 1
    return cnt


def left(i, j, G):
    cnt = 0
    if i == 0: return cnt
    for x in range(i - 1, -1, -1):
        if G[x][j] == 6:
            return cnt
        elif G[x][j] == 0:
            G[x][j] = 7
            cnt += 1
    return cnt


def down(i, j, G):
    cnt = 0
    if j == M - 1: return cnt
    for y in range(j + 1, M):
        if G[i][y] == 6:
            return cnt
        elif G[i][y] == 0:
            G[i][y] = 7
            cnt += 1
    return cnt


def up(i, j, G):
    cnt = 0
    if j == 0: return cnt
    for y in range(j - 1, -1, -1):
        if G[i][y] == 6:
            return cnt
        elif G[i][y] == 0:
            G[i][y] = 7
            cnt += 1
    return cnt


def find_blindspot(cctv, p, G):
    global empty
    empty_temp = empty
    #순열에 대해 cctv타입별로 비출방향을 정함
    for idx in range(len(p)):
        i, j, type = cctv[idx][0], cctv[idx][1], cctv[idx][2]
        if type == 4:
            turn = type4[p[idx]]
        elif type == 3:
            turn = type3[p[idx]]
        elif type == 2:
            turn = type2[p[idx]]
        else:
            turn = type1[p[idx]]
        # 비출방향을 하나씩 비춤 -> 0:상, 1:하, 2:좌, 3:우
        for d in range(len(turn)):
            dir = turn[d]
            if dir == 0:
                empty_temp -= up(i, j, G)
            elif dir == 1:
                empty_temp -= down(i, j, G)
            elif dir == 2:
                empty_temp -= left(i, j, G)
            else:
                empty_temp -= right(i, j, G)
            # 사각지대 없으면 멈추기
            if empty_temp == 0:
                return 0

    return empty_temp


import copy
# 각 cctv마다 비출 방향을 정하는 순열함수
def perm(p_num, k, cctv):
    global Min
    if Min == 0:
        return

    if p_num == k:
        copy_G = copy.deepcopy(org_G)
        min_temp = find_blindspot(cctv, p, copy_G)
        if min_temp < Min:
            Min = min_temp
        return

    else:
        i, j, type = cctv[k][0], cctv[k][1], cctv[k][2]
        # cctv 타입이 2일 때는 양쪽으로 경우의 수가 2가지
        if type == 2:
            for idx in range(2):
                p[k] = idx
                perm(p_num, k + 1, cctv)
        # 나머지 타입에 대해서는 경우의 수가 4가지씩
        else:
            for idx in range(4):
                p[k] = idx
                perm(p_num, k + 1, cctv)


N, M = map(int, input().split())
Min = 65

org_G = []
# 5번 cctv는 따로 계산할거라서 1~4번과 5번 cctv리스트를 따로만듬
cctv = []
cctv5 = []
# 남은 사각지대의 개수
empty = N * M
# cctv의 위치와 종류는 따로 저장, 빈 공간도 함께 계산
for i in range(N):
    temp = list(map(int, input().split()))
    org_G.append(temp)
    for j in range(M):
        if 0 < temp[j] < 7:
            empty -= 1
            if temp[j] == 5:
                cctv5.append([i, j, temp[j]])
            elif 0 < temp[j] < 5:
                cctv.append([i, j, temp[j]])

#cctv가 비출 수 있는 방향리스트
type1 = [[0], [1], [2], [3]]
type2 = [[0, 1], [2, 3]]
type3 = [[0, 2], [0, 3], [1, 2], [1, 3]]
type4 = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]

# cctv번호가 높을수록 사각지대가 많이 줄어드므로 먼저 계산할거라 cctv번호 내림차순으로 정렬
cctv.sort(key=lambda x: x[2], reverse=True)

# cctv 5번은 무조건 4방향이므로 처음에 계산해주고 시작
while cctv5:
    i, j, type = cctv5.pop()
    empty -= right(i, j, org_G)
    empty -= left(i, j, org_G)
    empty -= up(i, j, org_G)
    empty -= down(i, j, org_G)

# 각 cctv별로 비출 방향을 저장할 순열 리스트
p = [0] * len(cctv)
# 1~4번 cctv에 대해 순열구해서 최소값 찾기 시작
perm(len(cctv), 0, cctv)

print(Min)
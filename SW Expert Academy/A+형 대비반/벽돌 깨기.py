import sys
sys.stdin = open('dummy.txt','r')

import copy

def countarr(arr):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] : cnt+=1
    return cnt

def printarr(arr):
    for i in range(H):
        print(arr[i])
    print()

def f2_remove(j_idx,temp,br): # 영향받은 벽돌들 다 없애고 남은 벽돌들 끼리 붙이기\

    if j_idx == W :
        return
    else :
        for i in range(H):
            if not v[i][j_idx] and br[i][j_idx]:
                temp.append(br[i][j_idx])

        # top 갱신
        top[j_idx] = H - len(temp)


        # 벽돌 합치기
        for i in range(top[j_idx]):
            br[i][j_idx] = 0
        for i in range(len(temp)):
            br[top[j_idx]+i][j_idx] = temp[i]
        temp = []

        f2_remove(j_idx+1,temp,br)



def f1_bfs(q,br): # 영향 받은 벽돌들 다 표시하기
    if not q :
        return

    else : # 위에 정리 하면서 0으로 만들지말고 1보다 큰거만 append 처리하면서 여기서 다 블록을 없애 보자!!

        i, j, D = q.pop()
        v[i][j] = 1  # q로 받았으니 top 말고 q로
        br[i][j] = 0

        #영향 받은거 찾고
        if D > 1 :
            for d in range(1, D):
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x, y = i+dx*d, j+dy*d
                    if 0 <= x < H and 0 <= y < W and not v[x][y]:
                        if br[x][y] > 1 :
                            q.append((x,y,br[x][y]))
                        v[x][y] = 1
                        br[x][y] = 0

        f1_bfs(q,br)



def f0_Perm(n, k):
    global v, Min, br, top, br_cnt, Flag
    if not Flag : return
    if n == k :
        br = copy.deepcopy(bricks)
        top = copy.deepcopy(Top)
        #
        # print(arr/)
        for a in arr :
            if top[a] < H:
                v = [[0] * W for _ in range(H)]
                f1_bfs([(top[a],a,br[top[a]][a])], br)
                f2_remove(0, [], br)

                # print("after br")
                # printarr(br)
                # print("top:",top)
            else:
                continue
        if countarr(br) < Min:
            Min = countarr(br)
            if Min == 0 :
                Flag = False
                return
            # print("new Min:", Min)
        return

    else :
        for i in range(W):
            arr[n] = i
            f0_Perm(n+1,k)


T = int(input())
for tc in range(1, T + 1):
    N ,W, H = map(int,input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    Min = 1000000000000
    # 중복 순열로 공 떨어뜨릴 위치 구하기
    arr = [0]*N
    Flag = True
    #열마다 꼭대기 idx 구하기
    Top = [0]*W
    for j in range(W):
        flag = True
        for i in range(H):
            if bricks[i][j]:
                Top[j] = i
                flag = False
                break
        if flag : Top[j] = H-1

    f0_Perm(0, N)

    print("#{} {}".format(tc, Min))
import sys
sys.stdin= open("t.txt")

# def printarr(arr):
#     print("Start printing ")
#     for i in range(H):
#         print(arr[i])
#     print("end printing")

import copy
def br_count(arr):
    cnt =0
    for j in range(W):
        for i in range(H-1,-1,-1):
            if bricks[i][j] : cnt+=1
            else : break
    return cnt


def remove(n,k): #현재 j=w, 맨 마지막 열
    global bricks
    temp = []
    '''
    배열을 가로로 만들어서 
    '''
    if n==k :
        return

    else:
        for a in range(H):
            if bricks[a][n]:
                temp.append(bricks[a][n])
        for a in range(H-len(temp)):
            bricks[a][n] = 0
        for a in range(len(temp)):
            bricks[H-len(temp)+a][n] = temp[a]
        remove(n+1, k)




def bfs():
    global bricks, v
    '''
    perm에서 떨어지는 공의 위치에서 벽돌을 깨뜨리고 관련된 모든 벽돌을 다 0으로 만든다.
    만약 벽돌에 1이 아니면 그 벽돌을 저장, 벽돌숫자만큼 주위 벽돌에 0으로 만듬
    '''

    if q:
        i,j = map(int,q.pop(0))
        dis = bricks[i][j]

        if dis <= 1:
            bricks[i][j] = 0

        else :
            # print("i:{} j:{} dis:{}".format(i,j,dis))
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                for d in range(1,dis):
                    x, y = i + dx*d, j + dy*d
                    # print(d,"Go to",x,y)
                    if not (0 <= x < H and 0 <= y < W): continue
                    elif not v[x][y] and bricks[x][y] == 1: v[x][y] = 1; bricks[x][y] = 0
                    elif not v[x][y] and bricks[x][y] > 1: q.append((x,y))
                    v[x][y] = 1
            bricks[i][j] = 0
            bfs()







def perm(n,k): # n:현재, k:뽑고싶은 개수
    global bricks, Min, q, v
    if n==k:
        bricks = copy.deepcopy(Bricks)
        for j in P:
            for i in range(H):
                flag = False
                if bricks[i][j] :
                    if bricks[i][j] > 1 :
                        flag = True
                    q = [(i, j)]
                    v = [[0] * W for _ in range(H)]
                    v[i][j] = 1
                    bfs()
                    if flag :
                        remove(0, W)
                    break

        if Min > br_count(bricks):
            Min = br_count(bricks)
        return
    else :
        for i in range(W):
            P[n] = i
            perm(n+1,k)
            P[n] = 0

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int,input().split())
    Bricks = [[int(x) for x in input().split()] for _ in range(H)]
    P = [0]*N
    q = []
    Min = W*H
    perm(0, N)
    print("#{} {}".format(tc,Min))






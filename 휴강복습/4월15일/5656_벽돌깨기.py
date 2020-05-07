import sys
sys.stdin = open('t.txt', 'r')
'''
1. 공 떨어질 위치 정하기 - 중복 순열 : ball_perm()
2. 공이 떨어진 곳 벽돌 깨기 - 4방향 델타 dfs : brick_dfs()
3. 벽돌 깨지고 난 후 빈 공간 채우기 : organize()
- 새로운 행렬에 옮기기 or 버블솔트처럼 빈칸 이랑 자리 바꾸기 
'''
import copy
def printarr(arr):
    for i in arr:
        print(i)
    print()

def find_top(G,j):
    if not empty[j]:
        for i in range(H):
            if G[i][j] :
                return i, j
    empty[j] = 1
    return

def ball_perm(G,n,k):
    global  Min, org_flag,empty
    if n==k :
        if not Min: return
        G = copy.deepcopy(original_G)
        empty = [0] * W

        for a in arr:
            idx = find_top(G,a)
            if empty[a] :
                continue

            brick_dfs(G,*idx)
            if org_flag :
                organize(G)

            if G[H-1] == [0]*W :
                Min = 0
                return

        cnt = W*H
        for g in G :
            cnt-=g.count(0)

        if Min > cnt:
            Min = cnt
        return

    else :
        for j in range(W):
            arr[n] = j
            ball_perm(G,n+1,k)

def brick_dfs(G,i,j):
    global org_flag
    # 1.만약 벽돌이 1짜리면 그냥 자기만 0으로 바꿈
    if G[i][j] == 1 :
        G[i][j] = 0
        org_flag = False
        return
    # 2.만약 1보다 크면 그 길이만큼 벽돌 부수면서 1보다 큰 숫자 있으면 다음 dfs에 추가
    else :
        org_flag = True
        D = G[i][j]
        G[i][j] = 0

        for d in range(1,D):
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x, y = i+dx*d, j+dy*d
                if not( 0 <= x < H and 0 <= y <W ) or not G[x][y]: continue
                elif G[x][y] == 1 :
                    G[x][y] = 0

                else :
                    brick_dfs(G,x,y)

def organize(arr):
    #만약 지금 칸에 값이 없고 위에 값이 있으면 위아래 change
    for j in range(W):
        top = H-1
        for i in range(H-1,0,-1):
            if arr[i][j] :
                top-=1
            else :
                temp = top
                while not arr[temp][j]:
                    if temp == 0:
                        break
                    temp-=1
                arr[top][j], arr[temp][j] = arr[temp][j], arr[top][j]
                top-=1

T = int(input())
for tc in range(1,T+1):
    N, W, H = map(int,input().split())
    original_G = [[int(x) for x in input().split()] for _ in range(H)]
    arr = [0]*N
    Min = W*H
    empty = [0] * W
    org_flag = True
    G = copy.deepcopy(original_G)
    ball_perm(G, 0, N)

    print("#{} {}".format(tc,Min))
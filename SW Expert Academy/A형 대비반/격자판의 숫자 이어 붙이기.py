import sys
sys.stdin = open('dummy.txt','r')

# def cal(k,idx,temp):
#     print(k,idx,temp)
#     if k == 7 :
#         if temp not in nums:
#             nums.append(temp)
#             cnt+=1
#         temp = [num[0]]
#         return
#
#     else :
#         if idx >= 1 :
#             print("idx>1 -> idx-1")
#             cal(k + 1, idx-1,temp+[num[idx-1]])
#         if idx < 6:
#             print("idx<6> -> idx+1")
#             cal(k + 1, idx + 1, temp + [num[idx + 1]])

def bfs2(v,temp,n):

    Q.append(v)

    if len(temp) == 7 :
        print(temp)
        if temp not in result:
            result.append(temp)


        temp = [n[0]]
        return

    else :
        v = Q.pop(0)
        if v >= 1:
            Q.append(v-1)
            bfs2(v-1, temp + [n[v-1]], n)
        if v < 6:
            Q.append(v+1)
            bfs2(v+1, temp + [n[v+1]], n)


def bfs(x,y,num):

    if len(num) == 7 :
        if num not in nums:
            print("num",num)
            nums.append(num)
            bfs2(0,[num[0]],num)
        num = []
        return

    else :
        x, y = map(int,q.pop(0))
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            i,j = x+dx, y+dy
            if (0<=i<4 and 0<=j<4) and not v[i][j]:
                v[i][j] = v[x][y]+1
                q.append((i,j))
                bfs(i,j,num+[G[i][j]])




T = int(input())
for tc in range(1,T+1):
    G = [list(map(int,input().split())) for _ in range(4)]
    nums = []
    result = []
    Q = []
    # for x in range(4):
    #     for y in range(4):
    #         q = [(x, y)]
    #         v = [[0] * 4 for _ in range(4)]
    #         v[x][y] = 1
    #         bfs(x,y,[])
    q = [(0,0)]
    v = [[0] * 4 for _ in range(4)]
    v[0][0] = 1
    bfs(0, 0, [])

    print("#{} {}".format(tc,len(result)))
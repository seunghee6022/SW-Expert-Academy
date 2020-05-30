import sys
sys.stdin = open('색종이붙이기.txt', 'r')

def printarr(G):
    for i in range(10):
        print(G[i])
    print()

def paper_min_count(s_x,s_y,e_x,e_y, cnt,visited):
    print(s_x,s_y,e_x,e_y,visited[s_x][s_y])
    printarr(visited)
    global total_cnt
    print("cnt:",cnt)
    papercnt = 0
    temp_papers = [0, 0, 0, 0, 0, 0]
    if cnt>25 :

        for i in range(s_x, e_x+1):
            for j in range(s_y, e_y+1):
                if i>6 or j>6 or not visited[i][j]: continue
                flag = True
                for ii in range(i, i + 4):
                    for jj in range(j, j + 4):
                        if not visited[ii][jj]:
                            flag = False
                            break
                if not flag: continue
                for ii in range(i, i + 4):
                    for jj in range(j, j + 4):
                        visited[ii][jj] = 0
                papercnt += 1
                temp_papers[4] += 1
        print("after cnt>25:",temp_papers)
        printarr(visited)
    if cnt > 16:
        for i in range(s_x, e_x+1):
            for j in range(s_y, e_y+1):
                if i>6 or j>6 or not visited[i][j]: continue
                flag = True
                for ii in range(i, i + 4):
                    for jj in range(j, j + 4):
                        if not visited[ii][jj]:
                            flag = False
                            break
                if not flag: continue
                for ii in range(i, i + 4):
                    for jj in range(j, j + 4):
                        visited[ii][jj] = 0
                papercnt += 1
                temp_papers[4] += 1
        print("after cnt>16:",temp_papers)
        printarr(visited)
    if cnt > 9:
        for i in range(s_x,e_x+1):
            for j in range(s_y,e_y+1):
                if i > 7 or j > 7 or not visited[i][j]: continue
                if visited[i][j] and visited[i][j+1] and visited[i][j+2] and visited[i+1][j] and visited[i+1][j+1] and visited[i+1][j+2] and visited[i+2][j] and visited[i+2][j+1] and visited[i+2][j+2]:
                    for ii in range(i,i+3):
                        for jj in range(j,j+3):
                            visited[ii][jj] = 0
                    papercnt+=1
                    temp_papers[3]+=1
        print("after cnt>9:",temp_papers)
        printarr(visited)
    if cnt > 4 :
        for i in range(s_x,e_x+1):
            for j in range(s_y,e_y+1):
                if i > 8 or j > 8 or not visited[i][j]: continue
                if visited[i][j] and visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
                    papercnt += 1
                    temp_papers[2] += 1
                    visited[i][j] = 0
                    visited[i + 1][j] = 0
                    visited[i][j + 1] = 0
                    visited[i + 1][j + 1] = 0
        print("after cnt>4:",temp_papers)
        printarr(visited)


    # cnt < 4 인 것들에 대해
    for i in range(s_x, e_x + 1):
        for j in range(s_y, e_y + 1):
            if visited[i][j]:
                papercnt += 1
                temp_papers[1] += 1
    print("rest:")
    printarr(visited)

    if sum(temp_papers) > 25 : return -1
    for temp in temp_papers :
        if temp > 5: return -1
    for i in range(1,6):
        papers[i] -= temp_papers[i]
    print(papers)
    total_cnt+=papercnt
    printarr(Paper)


from collections import deque
def bfs(q):
    global total_cnt
    s_x, s_y = q[0][0], q[0][1]
    e_x,e_y = 0, 0
    cnt = 1
    Paper[s_x][s_y] = 0
    while q:
        i, j = map(int,q.popleft())
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            x, y= i+dx, j+dy
            if 0<=x<10 and 0<=y<10 and not visited[x][y] and Paper[x][y] :
                visited[x][y] = 1
                # check[x][y] = 1
                cnt += 1
                Paper[x][y] = 0
                q.append((x,y))
                if x > e_x : e_x = x
                if y > e_y : e_y = y
    # print(cnt)
    # printarr(visited)
    return  paper_min_count(s_x, s_y, e_x, e_y, cnt, visited)


import itertools
T = int(input())
for tc in range(1,T+1):
    total_cnt = 0
    Paper = [[int(x) for x in input().split()] for _ in range(10)]
    papers = [0,5,5,5,5,5]
    result = 0
    # print(tc,"번 색종이")
    # printarr(Paper)
    q = deque()

    for i in range(10):
        for j in range(10):
            if Paper[i][j]:
                visited = [[0] * 10 for _ in range(10)]
                q.append((i,j))
                visited[i][j] = 1
                result = bfs(q)
                if result == -1 : break

    if result == -1 :
        print("#{} {}".format(tc,-1))
    else :
        print("#{} {}".format(tc,total_cnt))

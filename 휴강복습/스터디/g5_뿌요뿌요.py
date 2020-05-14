import sys
sys.stdin = open('색종이붙이기.txt', 'r')


def printarr(G):
    for i in range(12):
        print(G[i])
    print()

def boom(i,j, color):
    global series, check_series, col_visited
    visited = [(i,j)]
    q = [(i,j)]
    cnt = 1
    col_visited.append(j)
    while q :
        i, j = map(int,q.pop())
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = i+dx, j+dy
            if 0 <= x < 12 and 0 <= y < 6 and G[x][y] == color and (x,y) not in visited :
                cnt+=1
                visited.append((x,y))
                q.append((x, y))
                if y not in col_visited:
                    col_visited.append(y)

    if cnt >= 4 :
        for v_x, v_y in visited:
            G[v_x][v_y] = '.'
            check_series += 1

    return

def down(col_visited):
    #한 열씩 밑에서부터
    global top
    temp_top = 0
    while col_visited:
        j = col_visited.pop()
        temp = []
        for i in range(11,top-1,-1):
            if G[i][j] != '.':
                temp.append(G[i][j])
                G[i][j] = '.'
        # 현재 뿌요의 최고 높이를 구하기 위함
        if temp_top < len(temp)-1:
            temp_top = len(temp)-1
        for i in range(len(temp)):
            G[-i-1][j] = temp[i]
    top = 11 - temp_top


# fixed matrix size 12*6
G = [[x for x in input()] for _ in range(12)]
top = 0
for i in range(12):
    if G[i].count('.') != 6 :
        top = i
        break
series = 0
col_visited = []
flag = True
while flag:
    col_visited = []
    check_series = 0
    for i in range(11,top-1,-1):
        for j in range(6):
            if G[i][j] != '.':
                boom(i,j,G[i][j])
    if not check_series:
        flag = False
        break
    down(col_visited)
    series += 1

print(series)


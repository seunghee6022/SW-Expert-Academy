T = int(input())
for tc in range(1,T+1):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]
    alist = []
    for i in range(n):
        for j in range(n):
            row = 0
            col = 0
            if data[i][j] != 0:
                while True:
                    row += 1
                    if i+row == n:
                        break
                    if data[i+row][j] == 0:
                        break
                while True:
                    col += 1
                    if j+col == n:
                        break
                    if data[i][j+col] == 0:
                        break
            if row != 0 and col != 0:
                for a in range(row):
                    for b in range(col):
                        data[i+a][j+b] = 0
                alist.append([row, col])
    blist = sorted(alist,key=lambda x : (x[0]*x[1],x[0]))
    print('#{} {}'.format(tc,len(blist)),end='')
    for q in blist:
        print(' ', end='')
        print(*q,end='')
    print()
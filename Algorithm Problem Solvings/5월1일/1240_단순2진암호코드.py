import sys
sys.stdin = open('t.txt','r')

T = int(input())
for tc in range(1,T+1):
    R,C = map(int,input().split())
    G = [[int(x) for x in input()] for _ in range(R)]

    code = [[[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)]
    code[3][2][1][1] = 0
    code[2][2][2][1] = 1
    code[2][1][2][2] = 2
    code[1][4][1][1] = 3
    code[1][1][3][2] = 4
    code[1][2][3][1] = 5
    code[1][1][1][4] = 6
    code[1][3][1][2] = 7
    code[1][2][1][3] = 8
    code[3][1][1][2] = 9


    s_x, s_y = 0, 0
    for i in range(R):
        for j in range(C-1,-1,-1):
            if G[i][j] == 1 :
                s_x, s_y = i, j
                break

    a, b, c, d, cnt = 0, 0, 0, 0, 0
    pw = []
    while s_y :
        if s_y >= 6 and G[s_x][s_y]:
            while G[s_x][s_y] :
                d+=1
                s_y-=1
                cnt+=1

            while not G[s_x][s_y]:
                c+=1
                s_y-=1
                cnt+=1
            while G[s_x][s_y]:
                b += 1
                s_y -= 1
                cnt += 1
            while not G[s_x][s_y] and cnt<7:
                a += 1
                s_y -= 1
                cnt += 1
            pw.append(code[a][b][c][d])
            a,b,c,d,cnt = 0,0,0,0,0
        else :
            break


    pw_confirmation = 0
    for i in range(8):
        if i & 1 :
            pw_confirmation += 3*pw[i]
        else :
            pw_confirmation += pw[i]
    if pw_confirmation % 10 :
        print("#{} {}".format(tc, 0))
    else :
        print("#{} {}".format(tc, sum(pw)))







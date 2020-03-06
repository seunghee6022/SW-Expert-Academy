import sys
sys.stdin = open("색칠하기.txt","r")

TC = int(input())
for tc in range(1,TC+1):
    N=int(input())          # 2~30

    datamap = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        r1,c1,r2,c2,color = map(int,input().split())        # r,c:0~9, r1<=r2, c1<=c2, color : 1 or 2(빨 or 파)
        for i in range(r1,r2+1):
            for j in range(c1,c2+1): datamap[i][j] |= color     # bitOR

    cnt_violet = 0
    for i in range(0, 10):
        for j in range(0,10):
            if datamap[i][j] == 0b11 : cnt_violet += 1          # 0b01 | 0b10

    print("#%d %d"%(tc,cnt_violet))
import sys
sys.stdin = open('dummy.txt','r')

def f (n,k,i,j,Sum):
    if n == k :
        result.add(Sum)
        Sum = 0
        return
    else :
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            x , y = i + dx, j + dy
            if 0<=x<4 and 0<=y<4 :
                f(n+1,k,x,y,Sum*10+G[x][y])




T = int(input())
for tc in range(1,T+1):
    G = [list(map(int,input().split())) for _ in range(4)]
    used = [[0]*4 for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            f(0,7,i,j,0)

    print("#{} {}".format(tc,len(result)))

import sys
sys.stdin = open('t.txt','r')

def printarr(arr):
    for i in range(N):
        print(arr[i])
    print()

def findmin(arr):
    global Min
    for i in range(N):
        Sum = sum(arr[i])
        if Sum < Min : Min = Sum
        if Min == 0 : return

from itertools import permutations
from copy import deepcopy
def spin(P, g, G):
    global Min

    for idx in P:

        r,c,s = map(int,spin_info[idx])
        s_x, s_y = r-s-1, c-s-1
        move_len = 2*s
        while move_len > 0 :

            for d in range(1,move_len+1):
                # right
                r_x, r_y = s_x, s_y
                g[r_x][r_y+d] = G[r_x][r_y+d-1]
                # down
                d_x,d_y = s_x,s_y+move_len
                g[d_x+d][d_y] = G[d_x+d-1][d_y]
                # left
                l_x,l_y = s_x+move_len, s_y+move_len
                g[l_x][l_y-d] = G[l_x][l_y-d+1]
                # up
                u_x, u_y = s_x+move_len, s_y
                g[u_x-d][u_y] = G[u_x-d+1][u_y]
            printarr(g)
            s_x+=1
            s_y+=1
            move_len -= 2
        G = deepcopy(g)
    # printarr(g)
    findmin(G)


N, M, K = map(int,input().split())
GG = [[int(x) for x in input().split()] for _ in range(N)]
perm = permutations(list(range(K)))
spin_info = []
for _ in range(K):
    spin_info.append(list(map(int,input().split())))

Min = 1000000000000
for P in perm :
    gg = deepcopy(GG)
    spin(P, gg, GG)

print(Min)
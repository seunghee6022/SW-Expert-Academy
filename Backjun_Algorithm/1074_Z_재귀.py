import sys
sys.stdin = open('dummy.txt','r')

def Z(N):
    global r,c,val
    print(A)
    if N == 1 :
        z = [[0] * 2 for _ in range(2)]
        for ii in range(2):
            for jj in range(2):
                z[ii][jj] = val
                val+=1
        print(z)
        return z
    else:

        for i in range(2):
            for j in range(2):
                print("i,j , N:",i,j, N)
                A[i][j] = Z(N-1)


N,r,c = map(int,input().split())
A = [[0] * 2 for _ in range(2)]
val = 0
z = [[0] * 2 for _ in range(2)]
Z(N)
for i in range(2):
    for j in range(2):
        print(A[i][j])


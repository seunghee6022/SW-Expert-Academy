import sys
sys.stdin = open('dummy.txt','r')

def printmat(mat):
    for i in range(N):
        for j in range(N):
            print(int(mat[i][j]%1000), end=' ')
        print()

def mat_sqrt(mat1,N,cnt):
    global M
    if cnt == M-1 :
       return printmat(mat1)

    result = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for c in range(N):
                result[i][j] += mat1[i][c]*A[c][j]
    mat_sqrt(result, N, cnt+1)

N, M = map(int,input().split())
A =[[int(x) for x in input().split()] for _ in range(N)]
mat_sqrt(A,N,0)

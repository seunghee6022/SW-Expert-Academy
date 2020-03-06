import sys
sys.stdin = open('dummy.txt','r')

N, M = map(int,input().split())
A =[[int(x) for x in input().split()] for _ in range(N)]
M, K = map(int,input().split())
B =[[int(x) for x in input().split()] for _ in range(M)]
mat = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for m in range(M):
            mat[i][j]+= A[i][m]*B[m][j]
        print(mat[i][j], end= ' ')
    print()


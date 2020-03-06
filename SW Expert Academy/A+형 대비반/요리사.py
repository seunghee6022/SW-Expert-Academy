import sys
sys.stdin = open('dummy.txt','r')




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    k=N//2
    C = [0]*k
    ing = [list(map(int,input().split())) for _ in range(N)]




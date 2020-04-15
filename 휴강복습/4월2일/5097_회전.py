import sys
sys.stdin = open('t.txt','r')

T = int(input())
for tc in range(1,T+1):
    L,N = map(int,input().split())
    q = [int(x) for x in input().split()]
    print("#{} {}".format(tc,q[N%L]))

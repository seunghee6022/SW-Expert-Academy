import sys
sys.stdin = open('dummy.txt','r')

T = int(input())
for tc in range(1,T+1):
    bus = [0]*5001
    N = int(input())
    for _ in range(N):
        start, end = map(int, input().split())
        for idx in range(start,end+1):
            bus[idx]+=1

    P = int(input())
    result =''
    for i in range(P):
        p = int(input())
        result+=str(bus[p])+' '

    print("#{} {}".format(tc,result[:-1]))
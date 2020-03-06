import sys
sys.stdin = open('dummy.txt','r')
T = int(input())
for tc in range(T):
    N = int(input())

    bus = [0] * 5001
    for _ in range(N):
        s, e = map(int, input().split())
        for i in range(s, e + 1):
            bus[i] += 1

    P = int(input())
    ans = []
    for _ in range(P):
        ans.append(str(bus[int(input())]))

    print("#{} {}".format(tc + 1, ' '.join(ans)))
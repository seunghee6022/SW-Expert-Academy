import sys
sys.stdin = open('dummy.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    n = input()
    wl = N//4
    n += n[:(wl)]
    res = set()
    for i in range(N):
        res.add(int(n[i:i+wl], 16))
    print(f'#{tc} {sorted(list(res))[-1*K]}')
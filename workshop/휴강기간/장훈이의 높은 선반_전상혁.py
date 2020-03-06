T = int(input())

for tc in range(T):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    result = 1000000000

    for i in range(1 << N):
        sum = 0

        for j in range(N):
            if i & (1 << j):
                sum += S[j]
        if sum == B:
            result = sum
            break
        elif sum > B and sum < result:
            result = sum

    print('#{} {}'.format(tc + 1, result - B))
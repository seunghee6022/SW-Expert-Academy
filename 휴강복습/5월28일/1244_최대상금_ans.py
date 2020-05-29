import sys
sys.stdin = open('1244_최대상금.txt','r')

def get_num():
    ret = 0
    for i in range(M):
        ret += 10 ** (M - i - 1) * nums[i]
    return ret


def swap(a):
    Q = []
    if a == N:
        return
    else:
        for i in range(M - 1):
            for j in range(i + 1, M):
                nums[i], nums[j] = nums[j], nums[i]
                temp = get_num()
                if temp not in visit[a]:
                    visit[a].add(temp)
                    swap(a + 1)
                nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for t in range(1, T + 1):
    nums, N = input().split()
    nums = list(map(int, list(nums)))
    M = len(nums)
    N = int(N)
    visit = [set() for _ in range(N)]
    Max = reversed(sorted(nums))
    swap(0)
    print('#{} {}'.format(t, max(visit[N - 1])))
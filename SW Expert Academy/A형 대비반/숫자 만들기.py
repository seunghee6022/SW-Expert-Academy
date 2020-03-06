import sys
sys.stdin = open('dummy.txt','r')

def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used, Sum, idx):
        global Min, Max
        if len(chosen) == r:
            if Sum > Max :
                Max = Sum
            if Sum < Min :
                Min = Sum

            Sum = nums[0]
            idx = 1

            return

        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i - 1] != arr[i] or used[i - 1]):
                chosen.append(arr[i])
                used[i] = 1
                num = nums[idx]
                if arr[i] == 0:
                    generate(chosen, used, Sum+num, idx + 1)
                elif arr[i] == 1:
                    generate(chosen, used, Sum-num, idx + 1)
                elif arr[i] == 2:
                    generate(chosen, used, Sum*num, idx + 1)
                else:
                    generate(chosen, used, int(Sum/num), idx + 1)
                used[i] = 0
                chosen.pop()

    generate([], used, nums[0], 1)


T = int(input())
for tc in range(1,T+1):
    N = int(input())

    op = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    Max, Min = -10000000, 10000000
    Oper=[] # 0:+, 1:-, 2:*, 3:/
    for i in range(4):
        for n in range(op[i]):
            Oper.append(i)

    Opers =[]
    permutation(Oper, N-1)

    print("#{} {}".format(tc,Max-Min))






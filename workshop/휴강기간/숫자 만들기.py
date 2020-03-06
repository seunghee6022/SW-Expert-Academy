import sys
# import itertools
sys.stdin = open('dummy.txt','r')


def permutation(arr, r):
    global count

    count = 0
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == r:
            c = chosen.copy()
            combi.append(c)

            global count
            count += 1
            return combi

        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i - 1] != arr[i] or used[i - 1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp =[int(x) for x in input().split()]
    idx = [range(N)]
    nums = [int(x) for x in input().split()]
    combi = []
    oper=[]
    for i in range(temp[0]):
        oper.append('+')
    for i in range(temp[1]):
        oper.append('-')
    for i in range(temp[2]):
        oper.append('*')
    for i in range(temp[3]):
        oper.append('/')

    permutation(oper, len(oper))

    max, min = -100000000 , 100000000

    for com in combi:
        sum = nums[0]

        for i in range(len(com)):
            if com[i] == '+':
                sum+=nums[i+1]
            elif com[i] == '-':
                sum -= nums[i+1]
            elif com[i] == '*':
                sum *= nums[i+1]
            elif com[i] == '/':
                sum = int(sum / nums[i+1])

        if sum > max : max = sum
        if sum < min : min = sum

    print("#{} {}".format(tc,max-min))









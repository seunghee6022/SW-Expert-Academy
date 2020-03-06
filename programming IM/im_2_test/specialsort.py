import sys
sys.stdin= open("specialsort.txt", 'r')

T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    result = []

    for j in range(5) :
        result.append(str(nums[-(j+1)]))
        result.append(str(nums[j]))

    print("#{} {}".format(i+1, ' '.join(result)))

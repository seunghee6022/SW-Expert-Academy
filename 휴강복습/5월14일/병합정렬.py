import sys
sys.stdin = open('병합정렬_input.txt','r')

def merge_sort(arr):
    global right_cnt
    if len(arr) == 1 :
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    global value, right_cnt

    if left[-1] > right[-1]:
        right_cnt += 1

    result = []
    i = j = 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1

            else :
                result.append(right[j])
                j += 1

        elif i < len(left):
            result.append(left[i])
            i += 1

        elif j < len(right):
            result.append(right[j])
            j += 1
    return result

T = int(input())
for tc in range(1,T+1):
    value, right_cnt = 0, 0
    N = int(input())
    arr = list(map(int,input().split()))
    result = merge_sort(arr)
    print("#{} {} {}".format(tc,result[N//2],right_cnt))


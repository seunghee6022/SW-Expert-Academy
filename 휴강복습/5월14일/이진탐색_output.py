# 이진검색 조건: 자료가 정렬되어 있어야 함

import sys
sys.stdin = open('이진탐색_input.txt','r')


def binarysearch(arr, key):
    global result

    low = 0
    high = len(arr) - 1
    mid = low + (low + high) // 2
    if arr[mid] == key:
        result += 1
        return
    # 일부러 반대로 저장해서 while문 시작하게
    # 오른쪽 = True
    elif arr[mid] < key:
        turn = False

    # 왼쪽 = False
    elif arr[mid] > key:
        turn = True

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            result += 1
            return mid
        # 오른쪽
        elif arr[mid] < key:
            if turn == False:
                turn = True
                low = mid + 1

            else:
                return -1
        # 왼쪽
        elif arr[mid] > key:
            if turn == True:
                turn = False
                high = mid - 1

            else:
                return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    result = 0
    for b in B:
        if b in A:
            binarysearch(A, b)
    print("#{} {}".format(tc, result))

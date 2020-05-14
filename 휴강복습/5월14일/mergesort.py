array = [2,4,7,4,6,1,10,9,8,3,5]

#문제를 절반으로 나누어 각각 해결하는 부분
def merge_sort(arr):
    # 크기가 1이면 더 이상 나눌 수 없다.
    if len(arr) == 1:
        return arr
    # 절반으로 나누어서 각각 별도의 정렬 실행
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    print(mid,left,right)

    # 분할정복 - 각각 나누어 해결함.
    left = merge_sort(left)
    right = merge_sort(right)
    print("left:",left,"right:",right)

    # return merge(left, right)
    print(merge2(left,right))
    return merge2(left,right)


#두개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
def merge(left, right):
    result = []

    # 병합과정 실행
    # 각각의 최소값들( 가장 앞쪽 값)을 비교해서 더 작은 요소를 결과에 추가
    # 두 부분집합에 요소가 없어질때 까지 계속 반복
    while left or right:
        # 두 부분집합의 요소가 모두 남아 있을 경우
        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else :
                result.append(right.pop(0))
        elif left:
            result.append(left.pop(0))
        elif right :
            result.append(right.pop(0))

    return result


# def mergesort(left, right):
#     result = []
#     while left or right:
#         if left and right:
#             if left[0] <= right[0] :
#                 result.append(right.pop(0))
#             else :
#                 result.append(left.pop(0))
#         elif left:
#             result.append(left.pop(0))
#         elif right:
#             result.append(right.pop(0))
#
#     return result

# 2. 인덱스로 접근하는 방법 - 인덱스 이동하면서 병합하는 함수
def merge2(left, right):
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





print(merge_sort(array))

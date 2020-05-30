def quick_sort(arr,left,right): #왼쪽 시작점, 오른쪽 끝지점
    # pivot 위치 결정(피봇을 기준으로 큰값은 오른쪽, 작은 값은 왼쪽으로 구분)
    # 왼쪽 부분집합 정렬
    #오른쪽 부분집합 정렬
    if left < right:
        #피봇구하기
        # pivot = hoare_partition(arr,left,right)
        pivot = lomuto_partition(arr, left, right)
        #왼쪽 부분집합 정렬 실행
        quick_sort(arr,left, pivot-1)
        #오른쪽 부분집합 정렬 실행
        quick_sort(arr,pivot+1,right)

def lomuto_partition(arr,left,right):
    #맨 오른쪽 요소를 pivot으로 설정하고,
    # i = left-1
    # j = 0
    pivot = arr[right]
    i = left -1

    # j는 left부터 right까지 1씩 증가
    for j in range(left,right):
        # arr[j]가 피벗보다 작으면,
        if arr[j] <= pivot:
            # i를 1 증가,
            i+=1
            # arr[j]와 arr[i]의 위치 교환
            arr[j], arr[i] = arr[i], arr[j]

    # i가 가리키는 위치가 피벗보다 작은 값의 마지막 인덱스
    # i+1위치에 pivot(arr[right])을 두고 i+1 반환
    arr[i+1] , arr[right] = arr[right], arr[i+1]
    return i+1

def hoare_partition(arr,left,right):
    i = left
    j = right
    # 맨 왼쪽 값이 피벗 값
    pivot = arr[left]

    #i가 j보다 작을 때 까지 계속해서 반복
    while i<=j:
        # 피봇보다 큰 값이 나올 때 까지 i증가
        while i<=j and arr[i] <= pivot:
            i += 1
        # 피봇보다 작은 값이 나올 때 까지 j감소
        while i<=j and arr[j] >= pivot:
            j -= 1

        #i가 j보다 작으면, 위치 교환
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

arr = [4,7,6,8,9,3,10,2,5]

quick_sort(arr,0,8)
print(arr)
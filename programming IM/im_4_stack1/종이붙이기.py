#중복 허용안하는 순열
def permutation(arr, r):
    global count
    count = 0
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == r:

            global count
            count +=1
            return

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

    w = int(input())
    w//=10
    #20종이 개수 - 일단 w를 20로 나눈 나머지와 몫으로 20짜리 종이를 몇개나 사용할 수 있는지 확인
    p2 = w//2
    #p2를 사용해서 p2종이의 개수에 따른 순열 조합의 수를 구함
    Sum = 1 #모두 10짜리만 쓰는 개수는 무조건 1
    for p in range(1,p2+1): #p는 20짜리 종이 개수 0부터 최대까지 (p가 0일 때는 이미 더했으므로 1부터 시작)
        arr = []
        # 총 종이 개수
        p_num = w-(p*2)+1 #총 w에서 20짜리 종이 길이를 빼면 1이 몇개인지 알 수 있고, 20짜리 종이 개수 더해줌
        arr.extend([1]*(w-(2*p)))
        arr.extend([2]*p)
        #case => 기본순열P(중복제거) = count * 20종이의 개수 = p * 2
        permutation(arr, len(arr))
        Sum += (2**p)*count

    print("#{} {}".format(tc,  Sum))
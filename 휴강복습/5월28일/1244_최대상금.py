import sys
sys.stdin = open('1244_최대상금.txt','r')

# 메모이제이션 저장하는 순열함수
import copy
def perm(k, n):
    global Max

    if k == n:
        return

    for i in range(k,len(prize)):
        prize[i], prize[k] = prize[k], prize[i]
        if prize not in memoi[k]:
            temp = copy.deepcopy(prize)
            memoi[k].append(temp)
            perm(k+1, n)
        prize[i], prize[k] = prize[k], prize[i]

# 메모이제이션에서 exchange-1 레벨에서 최대값 선정
def find_max(memoi, exchange):
    global Max
    if exchange > Len :
        Memoi = memoi[Len - 1]
    else :
        #메모이제이션 배열에 저장될 때 레벨 1씩 당겨서 저장되므로 exchange-1
        Memoi = memoi[exchange-1]
    Memoi.sort(reverse=True)
    # print(len(Memoi),Memoi)
    for pp in Memoi:
        t = 0
        for i in range(len(pp)):
            if i == 0 and pp[i] != max(pp): break
            t += pp[i]
            t *= 10
        t//=10
        if t > Max :
            Max = t
    return Max

T = int(input())
for tc in range(1,T+1):
    # prize : 상금 1자리씩 쪼개서 만든 배열
    prize_money , exchange = map(int,input().split())
    Len = len(str(prize_money))
    prize = []
    for i in range(Len) :
        prize.append(prize_money % 10)
        prize_money //= 10
    prize.reverse()

    # 메모이제이션 할 배열
    memoi = [[] for _ in range(10)]

    # 순열함수
    Max = 0
    perm(0, Len)

    # 메모이제이션에서 exchange-1 레벨에서 최대값 선정
    Max = find_max(memoi, exchange)

    print('#{} {}'.format(tc, Max))




import sys
sys.stdin = open('1244_최대상금.txt','r')
# 메모이제이션 저장하는 순열함수
def change_to_num(arr):
    num = 0
    l = len(arr)
    for i in range(l):
        num += arr[i]*10**(l-i-1)
    return num


def swap(k):
    # 순열을 나열하는게 아니라 깊이(exchange) 까지 내려가야함
    if k == exchange:
        return
    for i in range(Len - 1):
        for j in range(i + 1, Len):
            prize[i], prize[j] = prize[j], prize[i]
            num = change_to_num(prize)
            if num not in memoi[k]:
                memoi[k].add(num)
                swap(k + 1)
            prize[i], prize[j] = prize[j], prize[i]


T = int(input())
for tc in range(1, T + 1):
    # prize : 상금 1자리씩 쪼개서 만든 배열
    prize_money, exchange = map(int, input().split())
    Len = len(str(prize_money))
    prize = []
    for p in str(prize_money):
        prize.append(int(p))

    memoi = [set() for _ in range(10)]
    swap(0)
    print('#{} {}'.format(tc, max(memoi[exchange-1])))
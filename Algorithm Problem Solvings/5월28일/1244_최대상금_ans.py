import sys
sys.stdin = open('1244_최대상금.txt','r')

def swap(prize, i , j):
    numArr = [0]*numOfcard
    for k in range(numOfcard-1,-1,-1):
        numArr[k] = prize % 10
        prize //= 10

    #swap
    numArr[i], numArr[j] = numArr[j], numArr[i]

    #atoi
    prize = 0
    for k in range(numOfcard):
        prize = prize * 10 + numArr[k]
    return prize

def findMax(prize, num, k):
    global ans
    #메모이제이션 및 가지치기
    for i in range(MAXSIZE):
        if memo[k][i] == 0:
            memo[k][i] = prize
            break
        elif memo[k][i] == prize:
            return
    if k == num:
        if prize > ans: ans = prize

    else:
        for i in range(numOfcard - 1):
            for j in range(i + 1, numOfcard):
                findMax(swap(prize, i, j), num, k + 1)

MAXSIZE = 720
T = int(input())
for tc in range(1, T + 1):
    prize, num = map(int,input().split())
    memo = [[0] * MAXSIZE for _ in range(num+1)]
    numOfcard = 0
    ans = 0
    t= prize

    #숫자판의 자리수 구하기
    while(t):
        t //= 10
        numOfcard += 1

    findMax(prize,num,0)

    print('#{} {}'.format(tc,ans))
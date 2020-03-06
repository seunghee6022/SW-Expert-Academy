import sys
sys.stdin = open("subsum.txt", "r")

setA = list(range(1,13))
print(setA)
rev_A = sorted(setA ,reverse=True)

T = int(input())
for i in range(T):
    count = 0
    result = 0
    # N : 원소의 개수, K : 원소의 합
    N,K = map(int,input().split())

    for _ in range(N): #총 6번 실행
        for a in rev_A : #A 큰수부터 돌면서
            if K - a > 0:  #원소의 합에서-큰수
                K -= a
                count+=1
            elif K - a == 0 :
                if count != 6 : break
                else : result += 1
            else : break








    print("#{} {}".format(i+1,count))
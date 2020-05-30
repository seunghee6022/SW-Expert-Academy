import sys
sys.stdin = open('t.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    nums = input()
    nums = nums[-N//4+1:]+nums
    rank = set()

    for i in range(N):
        num = nums[i:i+N//4]
        res = 0

        for j in range(N//4):
            if num[-j-1].isalpha() :
                res+=(ord(num[-j-1])-ord("A")+10) * (16**j)
            else :
                res+=int(num[-j-1])*(16**j)

        rank.add(res)
    rank = sorted(list(rank),reverse=True)
    print(K-1,rank)


    print("#{} {}".format(tc,rank[K-1]))

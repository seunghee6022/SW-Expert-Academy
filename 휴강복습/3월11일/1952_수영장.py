import sys
sys.stdin = open('t.txt','r')

def pool(n,s):
    global Min

    if n >= 12:
        if Min > s :
            Min = s
        s = 0
        return

    else :
        # 1일권
        pool(n+1, s+(price[0]*schedule[n]))
        # 1달권
        pool(n+1, s+price[1])
        # 3달권
        pool(n+3, s+price[2])



T = int(input())
for tc in range(1,T+1):
    price = [int(x) for x in input().split()]
    schedule = [int(x) for x in input().split()]

    Min = price[-1] #1년치
    pool(0,0)


    print("#{} {}".format(tc,Min))
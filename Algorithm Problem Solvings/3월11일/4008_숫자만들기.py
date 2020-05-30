import sys
sys.stdin = open('t.txt','r')

def f(n,Sum,Sub,Mul,Div,s):
    global Max,Min

    if n == N :
        if Max < s : Max = s
        if Min > s : Min = s

        return

    else :
        if Sum > 0 :
            f(n+1,Sum-1,Sub,Mul,Div,s+nums[n])
        if Sub > 0 :
            f(n+1,Sum,Sub-1,Mul,Div,s-nums[n])
        if Mul > 0 :
            f(n+1,Sum,Sub,Mul-1,Div,s*nums[n])
        if Div >0 :
            f(n+1,Sum,Sub,Mul,Div-1,int(s/nums[n]))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    oper = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    Max, Min =  -100000000 , 100000000
    f(1, oper[0], oper[1], oper[2], oper[3], nums[0])
    print("#{} {}".format(tc,Max-Min))


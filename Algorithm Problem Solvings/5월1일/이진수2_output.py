import sys
sys.stdin = open("t.txt",'r')

T = int(input())
for tc in range(1,T+1):
    N = float(input())
    result = ''

    cnt = 1
    search = 1
    while N :
        if N >= search/2 :
            result+='1'
            N -= search/2
        else :
            result += '0'
        if len(result) >= 13 :
            result = 'overflow'
            break
        search/=2
    print("#{} {}".format(tc,result))

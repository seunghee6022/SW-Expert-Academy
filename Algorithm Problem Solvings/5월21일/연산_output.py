import sys
sys.stdin = open('연산_input.txt','r')

def cal(N,M,cnt, cal_num):
    global Min
    print(cnt,M,cal_num)
    if cnt >= Min :
        return

    elif cal_num == M :
        if cnt < Min :
            Min = cnt
        return

    else :
        if cal_num >= 1 :
            cal(N, M, cnt + 1, cal_num + 1)
            cal(N, M, cnt + 1, cal_num - 1)
            if cal_num < M :
                cal(N, M, cnt + 1, cal_num * 2)
            if cal_num > 10:
                cal(N, M, cnt + 1, cal_num - 10)


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    Min = 10000000000
    cal(N, M, 0, N)
    print("#{} {}".format(tc,Min))
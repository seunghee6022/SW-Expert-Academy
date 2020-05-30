import sys
sys.stdin = open('화물도크_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    application = []
    for n in range(N):
        application.append(list(map(int,input().split())))
    #종료시간 순으로 정렬
    application.sort(key = lambda x : x[1])
    # print(application)

    end_time = application[0][1]
    cnt = 1
    for app in application:
        if app[0] >= end_time and app[1] <= 24 :
            end_time = app[1]
            cnt+=1
    print("#{} {}".format(tc,cnt))

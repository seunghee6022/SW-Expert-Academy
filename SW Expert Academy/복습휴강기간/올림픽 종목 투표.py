import sys
sys.stdin = open('dummy.txt','r')

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    cate = list(map(int,input().split()))
    comm = list(map(int,input().split()))
    comm_cnt = [0] * M
    cate_cnt = [0]*N

    for i in range(M) :
        c = 0
        while not comm_cnt[i] and c<N :

            if comm[i] >= cate[c] :
                cate_cnt[c]+=1
                comm_cnt[i] = 1

            else : c +=1

    for c in range(N) :
        if cate_cnt[c] == max(cate_cnt):
            print("#{} {}".format(tc,c+1))
            break

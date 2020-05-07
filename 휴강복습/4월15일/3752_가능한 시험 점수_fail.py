import sys
sys.stdin = open('t2.txt','r')

import copy
def perm(n,k,num):
    if n==k :
        if num>1 :
            cal(arr)
        return
    else :
        arr[n] = 0
        perm(n+1,k,num)
        arr[n] = 1
        perm(n+1,k,num+1)


def cal(arr):
    tt = [0]
    add = []
    for i in range(len(arr)):
        if arr[i] :
            for s in s_temp[i]:
                # print(s)
                for t in tt :
                    # print(tt)
                    if s+t not in add :
                        # print(s,t,"s+t",s+t)
                        add.append(s+t)
                        # print(add)
            tt = copy.deepcopy(add)
        # print(tt)

    for a in add :
        if a not in scores:
            scores.append(a)
    # print("scores",scores)
    return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    info = {}
    scores = [0]
    score = list(map(int,input().split()))
    for s in score :
        if s in info.keys():
            info[s] += 1
        else:
            info[s] = 1
    # print(info)

    s_temp = []
    for key, val in info.items():
        temp = []
        for i in range(1,val+1):
            temp.append(key * i)
            if key*i not in scores :
                scores.append(key*i)
        s_temp.append(temp)
    # print(s_temp)

    arr = [0]*len(info)
    perm(0,len(info),0)

    print("#{} {}".format(tc,len(scores)))
import sys
sys.stdin=open('test.txt','r')

def dfs(n,k,cnt):
    global Max_cnt, info, temp
    print("temp , cnt:",temp,cnt)
    info.append(temp)
    # print("n:{} k:{} visited:{} cnt{}".format(n,k,visited,cnt))
    if n == k :
        print("n==k, cnt",k, cnt)
        if cnt > Max_cnt :
            Max_cnt = cnt
            print("Max")
            print(cnt,info)
            v_info = info
        info = []
        cnt = 0
        print(cnt)
        return

    for i in range(12):
        temp = ()
        print(i,temp)
        if i == 10:
            temp = (i, i + 1, 0)
        # 12월 일 때
        elif i == 11:
            temp = (i, 0, 1)
        else:
            temp = (i, i + 1, i + 2)
        print(temp)

        if not visited[temp[0]] and not visited[temp[1]] and not visited[temp[2]] and :
            for t in temp:
                visited[t] = 1
                info.append(t)
            dfs(n,k+1,cnt+(Plan[temp[0]]+Plan[temp[1]]+Plan[temp[2]]))






test = []
P = [int(x) for x in input().split()]
Plan =  [int(x) for x in input().split()]
Plan.extend((Plan[0],Plan[1]))
Max_cnt = 0
for m3 in range(1,4):
    print("m3:",m3)
    visited = [0]*12
    info, v_info = [], []
    temp = (0,1,2)
    Max_cnt = 0
    dfs(m3,0,0)
    print(v_info)


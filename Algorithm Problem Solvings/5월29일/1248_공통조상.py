import sys
sys.stdin = open('1248_공통조상.txt','r')

def comParent(info,v1,v2):
    v1_p = []
    cur1, cur2 = v1, v2
    cur_p1, cur_p2 = info[cur1][2], info[cur2][2]
    while cur1 != cur_p1:
        v1_p.append(cur_p1)
        cur1 = cur_p1
        cur_p1 = info[cur1][2]
    while cur2 != cur_p2 and cur2 not in v1_p:
        cur2 = cur_p2
        cur_p2 = info[cur2][2]

    return cur2

def treeSize(info, comP):
    global ans
    # left
    if info[comP][0]:
        treeSize(info,info[comP][0])
        ans+=1
    # right
    if info[comP][1]:
        treeSize(info, info[comP][1])
        ans += 1

T = int(input())
for tc in range(1,T+1):
    ans = 0
    V, E, V1, V2 = map(int,input().split())
    nodes = list(map(int,input().split()))
    #left, right, parent
    info = [[0]*3 for _ in range(V+1)]
    for i in range(E):
        p = nodes[2*i]
        c = nodes[2*i+1]
        if not info[p][0]:
            info[p][0] = c
        else:
            info[p][1] = c
        info[c][2] = p


    comP = comParent(info, V1, V2)
    treeSize(info, comP)

    print("#{} {} {}".format(tc,comP,ans+1))
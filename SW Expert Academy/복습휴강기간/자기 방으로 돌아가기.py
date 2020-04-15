import sys
sys.stdin = open("dummy.txt",'r')

def Perm(n, k): #현재까지 방에 간 학생, 총 학생 수
    global Max

    if n == k :
        print(order)
        cnt = 1
        for i1 in range(N-1):
            x1, y1 = map(int,room[order[i1]])
            for i2 in range(i1,N):
                x2, y2 = map(int, room[order[i2]])
                if not (x1<=x2<y1 or x1<=y2<y1):
                    cnt+=1

        if Max > cnt : Max = cnt
        cnt = 1

        return

    else :
        for i in range(N):
            if not used[i]:
                used[i] = 1
                order[n] = i
                Perm(n+1,k)
                used[i] = 0



T = int(input())
for tc in range(1,T+1):
    room = []
    N = int(input())
    Max = 400
    for n in range(N):
        x, y = map(int,input().split())
        room.append((x,y+1))
    check = [0]*N
    order = [0]*N
    used = [0]*N
    Perm(0,N)

    print("#{} {}".format(tc,Max))






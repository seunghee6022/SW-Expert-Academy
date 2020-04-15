import sys
sys.stdin = open("dummy.txt",'r')

def bfs(n, k, info):  # 현재까지 방에 간 학생, 총 학생 수
    global Max, cnt

    check[n] = 1
    # 모든 학생이 다 도착했으면
    if 0 not in check:
        if Max > cnt: Max = cnt
        cnt = 1
        return

    else:
        rx, ry = map(int, q.pop())
        # 같은 통로를 지나는 사람이 없으면
        for i in range(1, N):
            r = room[i]
            print("room:,",room)
            if not check[i] :
                if (rx <= r[0] < ry or rx <= r[1] < ry): cnt+=1; print("cnt up", cnt)
                q.append(r)
                bfs(n + 1, k, r)


T = int(input())
for tc in range(1, T + 1):

    room = []
    N = int(input())
    Max = 400
    cnt = 1
    for n in range(N):
        x, y = map(int, input().split())
        room.append((x, y + 1))
    q = [room[0]]
    check = [0] * N
    bfs(0, N, room[0])

    print("#{} {}".format(tc, Max))
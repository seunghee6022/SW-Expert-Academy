import sys
sys.stdin = open('dummy.txt','r')

#완전탐색 + 가지치기
def btk():
    Min = 10000000000000

    def dfs(m3, m1,cost):
        plan = Plan.copy()
        visited = [0] * 12
        # print("m3:{}, m1:{} , visited:{}".format(m3, m1, visited))


        # if  # 3개가 여러개일때 고르는 완전탐색 필요함

        v = q.pop(0)
        while 0 in visited or q :
            # print("V :", v)
            if v == 3 : #3개월치 끊을 때 (나중에 가지치기를 3달 아니면 거르는 걸로 하기)
                Max, Sum, temp = 0, 0, ()
                for i in range(0,12):
                    #3개 고르는 완전탐색 재귀 필요
                    # Sum = plan[i]+plan[i+1]+plan[i+2]
                    # if Sum > Max :
                    #     Max = Sum
                        # 11월 일 때
                        if i == 10 : temp = (i,i+1,0)
                        # 12월 일 때
                        elif i == 11: temp = (i, 0, 1)
                        else : temp = (i, i + 1, i + 2)

                for t in temp:
                    visited[t] = 1 # 3달 방문

                    plan[t] = 0 #계산 한 달 = 방문한 달은 0으로
                # print("i:{} ~ i+2:{}번째 달을 일일계산합니다 {}원.".format(i,i+2,cost))
                # print(visited)
                cost+=P[2]

            elif v == 2:  # 1개월치 끊을 때
                Max, Max_idx = 0, 0
                for i in range(12):
                    # print(plan[i])
                    if not visited[i] and plan[i]> Max:
                        Max = plan[i]
                        # print("Max:", plan[i])
                        Max_idx = i
                        # print("Max_idx:",Max_idx)
                    else : continue

                # print("Max_idx:{}번째 달을 1달치 계산합니다.{}원".format(Max_idx,cost))
                visited[Max_idx] = 1  # 1달 방문
                # print(visited)
                plan[Max_idx] = 0
                cost += P[1]

            else:  # 1일권 끊을 때
                for i in range(12):
                    if not visited[i]:

                        visited[i] = 1  # 1달 방문
                        # print(visited)
                        cost += P[0]*plan[i]
                        # print("i:{}번째 달을 일일계산합니다. {}회 {}원".format(i, plan[i], cost))
                        plan[i] = 0
            if q : v = q.pop(0)
        # print("m3:{}, m1:{} , dfs cost:{}".format(m3,m1,cost))
        return cost

    for m3 in range(4):
        q= []
        if m3:
            q.extend([3] * m3)
            # print("add m3")
        else : p = []
        for m1 in range(12 - 3 * m3):
            if m1:
                # print("add m1")
                q.extend([2] * m1)
                q.extend([1] * (12 - 3 * m3 - m1))
            else :
                # print("no m2, d1 :", (12-3*m3-m1))
                q.extend([1]*(12-3*m3-m1))
            # print(m3, m1, q)
            Cost = dfs(m3, m1,0)
            if Min > Cost : Min = Cost

    return Min



T = int(input())
for tc in range(1,T+1):
    P = [int(x) for x in input().split()]
    Plan =  [int(x) for x in input().split()]
    Plan.extend((Plan[0],Plan[1]))
    # print(plan)
    q = []


    print("#{} {}".format(tc,btk()))


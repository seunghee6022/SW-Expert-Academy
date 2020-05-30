import sys
sys.stdin = open('최소이동거리.txt','r')

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = {i:[] for i in range(V+1)}
    for _ in range(E):
        s,e,c = map(int,input().split())
        adj[s].append([e,c])

    INF = float('inf')
    dist = [INF] * V
    selected = [False] * V

    dist[0] = 0
    cnt = 0
    while cnt < V:
        # dist가 최소인 정점찾기
        min = INF
        u = -1
        for i in range(V):
            if not selected[i] and dist[i]<min:
                min = dist[i]
                u = i

        #결정
        selected[u] = True
        cnt += 1

        #간선완화
        for w,cost in adj[u]: #도착정점, 가중치
            if dist[w] > dist[u] +cost:
                dist[w] = dist[u]+cost
    print(dist)


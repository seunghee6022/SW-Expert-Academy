import sys
sys.stdin = open('최소신장트리.txt','r')
import heapq
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = {i:[] for i in range(V+1)}
    for _ in range(E):
        s,e,c = map(int,input().split())
        adj[s].append([e,c])
        adj[e].append([s,c])


    INF = float('inf')
    # 부모 초기화
    key = [INF] * (V+1)
    # 노드 방문 표시할 배열
    mst = [False]*(V+1)

    pq = []
    #시작 정점 0
    key[0] = 0
    result = 0
    heapq.heappush(pq,(0,0))
    print(pq)

    while pq:
        # 최소값 찾기
        k, node = heapq.heappop(pq)
        if mst[node] : continue
        mst[node] = True
        result += k
        print(result, k)
        # 가중치 갱신
        for dest, wt in adj[node]:
            print(dest, wt)
            if not mst[dest] : #우선순위큐가 이미 젤 작은걸 뱉어주므로 굳이 가중치 작은지 비교 필요없다.
            # if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                heapq.heappush(pq,(wt,dest)) #가중치, 정점

    print("#{} {}".format(tc,result))
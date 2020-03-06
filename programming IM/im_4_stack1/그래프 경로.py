import sys
sys.stdin = open('그래프 경로.txt','r')

def DFS(G,v):
    visited = [False]*(V+1)
    stack =[]
    stack.append(v)
    while len(stack) != 0 :
        v =stack.pop(-1)
        if not visited[v]:
            visited[v] = True
            # print("-",v,end="")
            for i in range(1,V+1):
                if not visited[i] and G[v][i]: stack.append(i)
    if visited[start] and visited[end] :return 1
    else : return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    G = [[0]*(V+1) for _ in range(V+1)]
    result = 0
    for e in range(E):
        i,j = map(int,input().split())
        G[i][j] = 1
    start, end = map(int,input().split())
    print("#{} {}".format(tc,DFS(G,start)))


import sys
sys.stdin = open('dummy.txt','r')

def triangle(v):
    global count,temp
    print(visited)
    if count == 3 and point in G[v]:
        temp = sorted(temp)
        if temp not in tri:
            tri.append(temp)
            print(temp)
        temp=[point]
        count=1
        return

    for w in range(v+1,N+1):
        if not visited[w] and w in G[v]:
            visited[w]=1
            count+=1
            temp.append(w)
            triangle(w)




T = int(input())
for tc in range(1,T+1):

    N, M = map(int,input().split())
    G = [[0] for _ in range(N+1)]
    tri = []
    temp=[]
    for _ in range(M):
        x, y = map(int,input().split())
        if 0 in G[x] :
            G[x].pop()
        G[x].append(y)
        if 0 in G[y] :
            G[y].pop()
        G[y].append(x)

    print(G)

    for i in range(1,N+1):
        visited = [0] * (N + 1)
        count = 1
        point = i
        temp = [point]
        print("point:",i)
        triangle(i)

    print(tri)
    print("#{} {}".format(tc,len(tri)))
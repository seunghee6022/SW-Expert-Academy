key[0] =
cnt = 0
result = 0
while cnt < V:
    min = INF
    u = -1
    for i in range(V):
        if not mst[i] and key[i] < min:
            min = key[i]
            u = i
    mst[u] = True
    result +=min
    cnt +=1

    for w in range(V):
        if adj[u][w] > 0 and not mst


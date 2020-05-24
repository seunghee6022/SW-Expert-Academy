import sys
sys.stdin = ('크루스칼')
'''
# makeset : 모든 정점에 대해 집합 생성
# 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때까지
# 간선을 선택 (!!! 사이클이 아닐 때만)
    # 사이클이면 스킵 : (사이클인거 아는 방법: )간선의 두 정점이 서로 같은 집합이면 ->findset이용
    # 사이클 아니면 간선 선택 : ->mst에 간선정보 더하기/ 두 정접을 합친다 -> union


'''

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x :
        return x
    else :
        # find_set(p[x])
        # pass compression
        p[x] = find_set(p[x])
        return p[x]

def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else :
        p[px] = py
        if rank[px] == rank[py]:
            rank[py]+=1

V,E = map(int,input().split())
# 간선들의 정보를 배열에 넣고 정렬시키기

# 일단 간선들의 정보 배열
edges = [list(map(int,input().split())) for _ in range(E)]
# print(edges)
# 간선을 간선가중치를 기준으로 오름차순 정렬
# key : 기준, 내가 x주면 넌 x의 두번째 정보만 알려줘
edges.sort(key = lambda x:x[2])
# print(edges)

# makeset : 모든 정점에 대해 집합 생성
p = [0] * V
rank = [0] * V
for i in range(V):
    make_set(i)
# 아래의 작업을 하기 전 모든 정점에 대해 makeset해야
cnt = 0
result = 0
mst=[]
# 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때까지
for i in range(E):
    s,e,c = edges[i][0], edges[i][1], edges[i][2]
    # 사이클이면 스킵 : (사이클인거 아는 방법: )간선의 두 정점이 서로 같은 집합이면 ->findset이용
    if find_set(s) == find_set(e): continue
    # 간선 선택
    # mst에 간선정보 더하기/ 두 정접을 합친다.union
    result += c
    mst.append(edges[i])
    union(s,e)

    cnt += 1
    if cnt == V-1 : break

print(result)
print(mst)



'''
1. 섬에서 모든 다리,그 가중치 기록해서 그래프로 만든다.
2. 그래프 MST최소 신장 트리 만들기

섬 리스트 - 섬 연결 체크
'''
import sys
sys.stdin = open('t.txt','r')

def printarr(arr):
    for i in range(N):
        print(arr[i])
    print()

from collections import deque
def check_sea_bfs():
    global island_num
    # 섬 넘버링, 다리 놓을 위치와 방향 저장
    while q:
        i, j = map(int,q.popleft())
        for direct in range(4):
            x, y = i+dx[direct], j+dy[direct]
            if (0 <= x < N and 0 <= y < M) and not G[x][y]:
                #다리를 시작할 바다의 위치, 다리 놓을 방향 같이 저장
                island_sea[island_num].append((x,y,direct))
            elif (0 <= x < N and 0 <= y < M) and G[x][y] and not v[x][y]:
                q.append((x, y))
                v[x][y] = island_num


def build_bridge_bfs():
    global next_island, island_num, w, cur_dir
    # 방향대로 다리를 놓기. 길이 1이면 패스
    for cur_island in range(1,island_num):
        # print("cur_island is",cur_island)
        while island_sea[cur_island]:
            d, w = 1, 1
            i, j, direct = map(int,island_sea[cur_island].pop())
            if direct == 0 or direct == 1:  #가로
                cur_dir = 7
            else : cur_dir = 8
            v[i][j] = cur_dir #세로
            x, y = i+dx[direct]*d, j+dy[direct]*d
            # 땅에 닿을 때 까지, direct값을 v에 넣으면
            # 값 중복 안되게 하기 위해서 방향 정보가 가로7, 세로8 로 visit에 들어갈 것이다.
            #길이2부터 시작하므로, 땅이있다 == 다리길이 1 : 멈춤
            if not (0 <= x < N and 0 <= y < M) or G[x][y] : continue
            #아니면 시작한다.
            flag = False
            # 다리 놨던 방향x. (방문 안했거나, 교차할 때 확인)
            while (0 <= x < N and 0 <= y < M) and v[x][y] != cur_dir:
                if not G[x][y]: #, 바다 -> 계속 가기
                    d += 1
                    w += 1
                    v[x][y] = cur_dir
                else : # 섬을 만나면
                    flag = True
                    next_island = v[x][y]
                    break
                x, y = i + dx[direct] * d, j + dy[direct] * d

            if flag:
                bridge.append([w,cur_island,next_island])

        cur_island+=1


class UF:
    def __init__(self, N):
        self._id = [i for i in range(N)]

    # judge two node connected or not
    def connected(self, p, q):
        return self._find(p) == self._find(q)

    # quick union two component
    def union(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root

    # find the root of p
    def _find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p

def kruskal(G):
    # initialize MST
    MST = set()
    len_cnt, edges = 0, 0
    uf = UF(island_num)
    for b in bridge:
        u, v = b[1], b[2]
        # if u, v already connected, abort this edge
        if uf.connected(u, v):
            continue
        # if not, connect them and add this edge to the MST
        uf.union(u, v)
        edges+=1
        MST.add((u,v))
        v_island[u] = 1
        v_island[v] = 1
        len_cnt += b[0]
    if v_island[1:] == [1]*(island_num-1) and edges == island_num-2 : return len_cnt
    return -1



N, M = map(int,input().split())
G = []
land = []
for i in range(N):
    temp = [int(x) for x in input().split()]
    G.append(temp)
    # 땅을 기록 : 나중에 bfs에서 시작점으로 이용하기 위해
    for j in range(M):
        if temp[j] == 1 : land.append((i,j))

if not len(land): print(-1)
else:
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    #섬을 넘버링 하기 위해
    island_num = 1
    island_sea = [[] for _ in range(7)]
    v = [[0]*M for _ in range(N)]
    for i,j in land:
        if not v[i][j]:
            q = deque()
            q.append((i,j))
            v[i][j] = island_num
            check_sea_bfs()
            island_num+=1
    # printarr(v)


    '''
    1. 섬에서 모든 다리, 그 가중치를 기록하는 방법
    섬 - 노드
    다리 - 간선
    다리 길이 - 가중치
    1-1. 섬인 점들을 기록한다..
    1-2. 섬인 점들에서 4방향으로 모든 가능한 바다를 찾는다.
        1-2-1 바다를 찾아서 bfs에 넣을 때, 만약 같은 라인에 섬이 있을 때 넣는 방법은 최적화에서 사용
    1-3. bfs시작해서 다음 섬까지 도달하면 그 섬은 +1해서 섬의 땅 숫자를 넘버링한다.
        그리고 같은 방법으로 바다를 찾고 다음 섬에 도달한다.
    '''

    # 다리 정보 저장된 그래프
    bridge = []
    b_items_cnt = 0
    build_bridge_bfs()
    bridge.sort(key=lambda x:x[0])

    #최소 거리 구하기
    Min = 987654321
    v_island = [0]*island_num
    flag = False
    print(kruskal(bridge))


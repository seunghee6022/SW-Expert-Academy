import sys
sys.stdin = open('작업관리.txt','r')

'''
모든 경로가 다 방문이면 그 노드 출력. 노드가 1개인건 바로 출력 아닌건 continue해서 다음에 다른 노드로부터 방문을
받아야만 비로소 모든 경로가 방문으로 되어 출력가능해지게 코드
두 노드가 연결되어있는 것이 나오면 중단
하나씩 탐색하다가
@ 4, 8는 자기에게 아무것도 연결되어있지 않다.
1. 4부터 시작

4->1 1->2 and 5 근데 5가 다른 노드로부터도 연결되어 있으므로 5에서 뻗어진 노드와 관련있는 노드 다 불가
(그런데 1->5가 갔다는 것에 True가 되어있어야 다음에 8->5 갔을 때 모두 방문으로 되어서 5도 된다.)
2->3 and 7 ,7은 하나만 연결되어있으므로 7->6 인데 밑 6노드가 두개랑 연결되어 있으므로 7도 안됨다.
(만약 2-> 7 갔다가 7다음 노드에 2개가 연결되어 있으면 7도 출력 x)
(그러나 7->6 : 방문 True)

2. 8 시작
8-> 5   1,8 모두에서 5한테 갔으므로 ok
5-> 6   5,7 모두에서 6한테 갔으므로 ok
8-> 9 
 
'''
def DFS(G,start):
    visited = [False] * (V + 1)
    stack = []
    result = ''
    while len(start) :
        v = start.pop(-1)
        stack.append(v)
        while len(stack) :
            v = stack.pop(-1)
            if not visited[v]:
                visited[v] = True
                result+=str(v)+' '
                for i in range(1,V+1):
                    if not visited[i] and G[v][i] :
                        flag = True
                        for k in range(1,V+1):
                            if G[k][i] and visited[k]==False: flag = False; break
                        if flag == True : stack.append(i)
    return result[:len(result)-1]

for tc in range(1,11):
    V , E = map(int,input().split())
    info = list(map(int,input().split()))
    G = [[0]*(V+1) for _ in range(V+1)]
    for i in range(0,2*E,2):
        G[info[i]][info[i+1]] = 1
    start = []
    for j in range(1,V+1):
        flag = True
        for i in range(1,V+1):
            if G[i][j] : flag = False ; break
        if flag == True : start.append(j)
    print("#{} {}".format(tc,DFS(G, start)))





import sys
sys.stdin = open('dummy.txt','r')

#배운점 :  visited를 쓸 필요 없고 G자체에서 왔던 곳을 0으로 만들어주기
#sord 람다식 조건 두개 쓸 수 있다
#unpack활용 좋다.

def search_mat(x, y):
    global m_cnt
    e_r, e_c = 0, 0
    for i in range(x, n):
        if G[i][y]:
            if i != n - 1 and G[i + 1][y]:
                continue
            else:
                e_r = i
                break

    for j in range(y, n):
        if G[x][j]:
            if j != n - 1 and G[x][j + 1]:
                continue
            else:
                e_c = j
                break
    m_cnt += 1
    a_list.append([e_r - x + 1, e_c - y + 1])
    for i in range(x, e_r + 1):
        for j in range(y, e_c + 1):
            G[i][j] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    G = [[int(x) for x in input().split()] for _ in range(n)]

    a_list = []
    m_cnt = 0
    for x in range(n):
        for y in range(n):
            if G[x][y]:
                search_mat(x, y)

    ans = sorted(a_list, key=lambda x: (x[0] * x[1], x[0]))
    result = []
    for i in ans:
        result.append(str(i[0]))
        result.append(str(i[1]))

    print("#{} {} {}".format(tc, m_cnt, ' '.join(result)))



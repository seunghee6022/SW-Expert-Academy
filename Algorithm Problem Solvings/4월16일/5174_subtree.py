import sys
sys.stdin = open("subtree_input.txt", "r")
def preorder_cnt(node):
    global cnt
    if node != 0:
        cnt+=1
        # print(f"{node}", end=" ")
        preorder_cnt(tree[node][0])
        preorder_cnt(tree[node][1])

# def printTree():
#     for i in range(1, E+2):
#         print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))

T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())
    tree = [[0]*3 for _ in range(E+2)]
    temp = list(map(int, input().split()))
    for i in range(E):
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1

    cnt = 0
    preorder_cnt(N)
    print("#{} {}".format(tc,cnt))



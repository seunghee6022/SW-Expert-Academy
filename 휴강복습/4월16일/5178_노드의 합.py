import sys
sys.stdin = open("노드의 합_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    leaf_list = []
    for i in range(M):
        leaf, val = map(int,input().split())
        leaf_list.append(leaf)
        tree[leaf] = val

    leaf = N
    while leaf != 1 :
        tree[leaf//2]+=tree[leaf]
        leaf-=1

    print("#{} {}".format(tc,tree[L]))



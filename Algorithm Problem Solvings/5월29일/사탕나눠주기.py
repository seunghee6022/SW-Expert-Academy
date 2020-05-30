import sys
sys.stdin = open('사탕나눠주기.txt','r')
'''
어린이들이 보유한 사탕 종류의 합이 최대가 되는 프로그램.
서로 다른 종류의 사탕을 한 개씩 나눠줄 수 있으며,
사탕 종류 < 어린이 : 앞의 어린이 M명한테만 나눠줌
'''

# 나눠줄 사탕의 종류를 정할 순열함수
# type을 인자로 넣어서 개수를 Max와 비교
def candyPerm(n,k,type):
    global Max

    if n==k:
        # type과 Max와 비교해서 갱신
        if Max < type :
            Max = type
        return
    else:
        for i in range(1,M+1):
            if not v[i]:
                v[i] = 1
                p[k] = i
                # 만약 k번째 아이에게 줄 사탕이 그 아이에게 없는 종류면 type+1
                if not children[k][i]:
                    candyPerm(n, k + 1, type + 1)
                # 만약 k번째 아이에게 줄 사탕이 그 아이에게 있다면 그대로
                else:
                    candyPerm(n, k + 1, type)
                v[i] = 0




T = int(input())
for tc in range(1,T+1):
    ans = 0
    N, M = map(int,input().split())
    # 각 아이들이 가지고 있는 사탕의 종류와 개수를 담을 리스트
    children = []
    # 아이들이 가지고있는 사탕 종류 총 수
    type = 0
    # 아이 한 명씩 사탕의 종류와 갯수를 child리스트에 넣고 children에 추가
    for i in range(N):
        child = [0] * (M + 1)
        candy = [int(x) for x in input().split()]
        for c in candy[1:]:
            child[c]+=1
        children.append(child)
        # 배열의 크기- 없는 사탕종류의 수를 type에 계속 더해준다.
        type += (M+1-child.count(0))

    # 처음에 Max의 default: 사탕을 나눠받기 전 총 사탕종류 수로 지정
    Max = type
    v = [0]*(M+1)
    # 아이들 수 > 사탕 종류 수
    if N > M :
        p = [0]*M
        candyPerm(M, 0, type)
    # 아이들 수 < 사탕 종류 수
    else :
        p = [0]*N
        candyPerm(N, 0, type)

    print("#{} {}".format(tc,Max))
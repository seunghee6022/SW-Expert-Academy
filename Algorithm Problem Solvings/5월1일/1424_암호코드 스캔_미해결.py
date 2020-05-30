import sys
sys.stdin = open('t.txt','r')

# def find_startidx(G, R, C):
#     pws=[]
#     for i in range(1,R-1):
#         for j in range(C-1, 0, -1):
#             if G[i][j] != '0' and G[i-1][j]=='0' and G[i][j+1] == '0':
#                 print(i,j,G[i][j])
#                 pws.append([i, j])
#     # print(pws)
#     return pws
#
#
#
#
# def pw_to_binary(idx):
#     print(idx)
#     s_x, s_y = map(int, idx)
#     product_num = []
#     pw = ''
#     while G[s_x][s_y] != '0' :
#         pw+=G[s_x][s_y]
#         s_y-=1
#     print(pw[::-1])
#     binary_pw = ''
#     for key in pw[::-1]:
#         binary_pw+=mapping[key]
#
#     print(binary_pw)
#
#     j = len(binary_pw)-1
#     a, b, c, d, cnt = 0, 0, 0, 0, 0
#     while j >= 0 :
#         if binary_pw[j] == '1' :
#             while binary_pw[j] == '1' :
#                 d += 1
#                 cnt += 1
#                 j -= 1
#             while binary_pw[j] == '0':
#                 c += 1
#                 cnt += 1
#                 j -= 1
#             while binary_pw[j] == '1' :
#                 b += 1
#                 cnt += 1
#                 j -= 1
#             while binary_pw[j] == '0' and cnt < 7 :
#                 a += 1
#                 cnt += 1
#                 j -= 1
#             # print(a,b,c,d,"->",code[a][b][c][d])
#             product_num.append(code[a][b][c][d])
#             a, b, c, d, cnt = 0, 0, 0, 0, 0
#
#         else :
#             j -= 1
#     print(product_num[::-1])
#     return product_num[::-1]
#
# def check_pw(product_num):
#     check = 0
#     for i in range(7):
#         if i & 1 :
#             check += product_num[i]
#         else :
#             check += 3*product_num[i]
#     check += product_num[7]
#     if  check% 10 :
#         return False
#     else :
#         print("#{} {}".format(tc, sum(product_num)))
#         return True
#
#
# mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#                '8': '1000', '9': '1001', 'A': '1010', 'a': '1010', 'B': '1011', 'b': '1011', 'C': '1100', 'c': '1100',
#                'D': '1101', 'd': '1101', 'E': '1110', 'e': '1110', 'F': '1111', 'f': '1111'}
#
# T = int(input())
# for tc in range(1,T+1):
#     R,C = map(int,input().split())
#     G = [[x for x in input()] for _ in range(R)]
#
#     code = [[[[0 for _ in range(5) ] for _ in range(5)] for _ in range(5)]for _ in range(5)]
#     code[3][2][1][1] = 0
#     code[2][2][2][1] = 1
#     code[2][1][2][2] = 2
#     code[1][4][1][1] = 3
#     code[1][1][3][2] = 4
#     code[1][2][3][1] = 5
#     code[1][1][1][4] = 6
#     code[1][3][1][2] = 7
#     code[1][2][1][3] = 8
#     code[3][1][1][2] = 9
#
#     pws = find_startidx(G, R, C)
#     flag = False
#     while not flag :
#         product_num = pw_to_binary(pws.pop())
#         flag = check_pw(product_num)

def find_startidx(G, R, C):
    pws=[]

    for i in range(1,R-1):
        cnt = 0
        for j in range(C-1, 0, -1):
            if G[i][j] != '0' and G[i-1][j]=='0' and G[i][j+1] == '0' :
                print(i, j, G[i][j])
                if not cnt :
                    print(i,j,G[i][j])
                    pws.append([i, j])
                else
                cnt+=1
    print(pws)
    return pws

# 패스워드가 시작하는 시작점들 찾아 리스트pws 만들기
def find_startidx(G, R, C):
    pws = []

    for i in range(1, R - 1):
        cnt = 0
        j = C - 1
        temp = ''
        while j :
            # 뒤에서부터 찾아서 시작점만 저장 - 오른쪽과 위쪽 = 코너 모두가 0이면 시작점
            if G[i][j] != '0' and G[i - 1][j] == '0' and G[i][j + 1] == '0' and not cnt:
                print(i, j, G[i][j])
                while cnt < 15 :
                    temp+=G[i][j]
                    j-=1
                    if cnt == 14 :
                        cnt += 1
    print(pws)
    return pws

def pw_to_binary(idx):
    s_x, s_y = map(int, idx)
    product_num = []
    pw = ''
    while G[s_x][s_y] != '0' :
        pw+=G[s_x][s_y]
        s_y-=1

    binary_pw = ''
    for key in pw[::-1]:
        binary_pw+=mapping[key]
    print(pw)


    j = len(binary_pw)-1
    div = (j+1)//56
    print(j, div)
    if not div : return False

    a, b, c, d, cnt = 0, 0, 0, 0, 0
    while j >= 0 :
        if binary_pw[j] == '1' :
            while binary_pw[j] == '1' :
                d += 1
                cnt += 1
                j -= 1
            while binary_pw[j] == '0':
                c += 1
                cnt += 1
                j -= 1
            while binary_pw[j] == '1' :
                b += 1
                cnt += 1
                j -= 1
            while binary_pw[j] == '0' and cnt < 7 :
                a += 1
                cnt += 1
                j -= 1
            product_num.append(code[a//div][b//div][c//div][d//div])
            a, b, c, d, cnt = 0, 0, 0, 0, 0
        else :
            j -= 1

    return product_num[::-1]

def check_pw(product_num):
    check = 0
    for i in range(7):
        if i & 1 :
            check += product_num[i]
        else :
            check += 3*product_num[i]
    check += product_num[7]
    if  check% 10 :
        return False
    else :
        print("#{} {}".format(tc, sum(product_num)))
        return True


mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'a': '1010', 'B': '1011', 'b': '1011', 'C': '1100', 'c': '1100',
               'D': '1101', 'd': '1101', 'E': '1110', 'e': '1110', 'F': '1111', 'f': '1111'}

T = int(input())
for tc in range(1,T+1):
    R,C = map(int,input().split())
    G = [[x for x in input()] for _ in range(R)]

    code = [[[[0 for _ in range(5) ] for _ in range(5)] for _ in range(5)]for _ in range(5)]
    code[3][2][1][1] = 0
    code[2][2][2][1] = 1
    code[2][1][2][2] = 2
    code[1][4][1][1] = 3
    code[1][1][3][2] = 4
    code[1][2][3][1] = 5
    code[1][1][1][4] = 6
    code[1][3][1][2] = 7
    code[1][2][1][3] = 8
    code[3][1][1][2] = 9

    pws = find_startidx(G, R, C)
    print(pws)
    flag = False
    while not flag and len(pws) :
        idx = pws.pop()
        product_num = pw_to_binary(idx)
        if not product_num : continue
        flag = check_pw(product_num)
    if not flag: print("#{} {}".format(tc, 0))


import  sys
sys.stdin = open("palindrome.txt", "r")

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    result = ''

    #2차원 배열 만들기
    pal = [0] * N
    for k in range(N):
        pal[k] = [0] * N
    #문자 넣기
    for r in range(N):
        line = input()
        for c in range(N):
            pal[r][c] = line[c]
    #print(pal)

    #회문 찾기- 가로부터
    r_result = ''
    for rr in range(N):
        for cc in range(0,round(M/2)):
            if pal[rr][cc] != pal[rr][-(cc+1)]:
                break
            else:
                print("pal[{}][{}] and pal[{}][{}]".format(rr,cc,rr,-(cc+1)))
                print("{}=={} add".format(pal[rr][cc],pal[rr][-(cc+1)]))
                r_result += pal[rr][cc]

        if len(r_result) == round(M/2) :
            for p in range(round(M/2),0,-1):
                r_result+=r_result[p-1]
            result = r_result
        else : r_result = ''
    print("result : {}".format(result))

    # 회문 찾기- 세로
    c_result = ''
    for cc in range(N):
        for rr in range(0, round(M / 2)):
            if pal[rr][cc] != pal[-(rr+1)][cc]:
                break
            else:
                print("pal[{}][{}] and pal[{}][{}]".format(rr, cc, -(rr+1), cc))
                print("{}=={} add".format(pal[rr][cc], pal[-(rr+1)][cc]))
                c_result += pal[rr][cc]

        if len(c_result) == round(M / 2):
            for p in range(round(M / 2), 0, -1):
                c_result += c_result[p - 1]
            result = c_result
        else:
            c_result = ''

    print(c_result)
    # for pp in range(int(M/2), 0, -1):
    #     c_result += c_result[pp - 1]



    if result == '':
        print("회문이 없습니다.")
    else :
        print("#{} {}".format(i+1,result))

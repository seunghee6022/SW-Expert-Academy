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
        for cc in range(0,N-M+1):
            for kk in range(M):
                if pal[rr][cc+kk] != pal[rr][M+cc-1-kk]:
                    break
                else:
                    print("pal[{}][{}] and pal[{}][{}]".format(rr,cc+kk,rr,M+cc-1-kk))
                    print("{}=={} add".format(pal[rr][cc+kk],pal[rr][M+cc-1-kk]))
                    r_result += pal[rr][cc+kk]
                print("r_result:{}".format(r_result))
            if len(r_result) == M :
                result = r_result

            r_result = ''
            print("r_result:{}".format(r_result))
    print("result : {}".format(result))

    # 회문 찾기- 세로
    c_result = ''
    for cc in range(N):
        for rr in range(0, N - M + 1):
            for kk in range(M):
                if pal[rr+kk][cc] != pal[rr+M-1-kk][cc]:
                    break
                else:
                    print("pal[{}][{}] and pal[{}][{}]".format(rr+kk, cc , rr+M-1-kk, cc))
                    print("{}=={} add".format(pal[rr+kk][cc], pal[rr+M-1-kk][cc]))
                    c_result += pal[rr+kk][cc]


            if len(c_result) == M:
                result = c_result
            c_result = ''
        print("c_result:{}".format(c_result))


    if result == '':
        print("회문이 없습니다.")
    else :
        print("#{} {}".format(i+1,result))

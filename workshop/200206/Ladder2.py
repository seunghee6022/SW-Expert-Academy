import sys
sys.stdin  = open("Ladder2.txt","r")

def left_right(h,w,ladder):
    if w == 0:
        left = False
        # print("w=0라서 left => False")
        if ladder[h][w + 1] == 1:
            right = True
        else:
            right = False

    if w == 99:
        right = False
        # print("w=99라서 right => False")
        if ladder[h][w - 1] == 1:
            left = True
        else:
            left = False

    # 오른쪽부터 살피기
    if 0 < w < 99:
        if ladder[h][w + 1] == 1:
            right = True
            left = False
        else:
            right = False

        if ladder[h][w - 1] == 1:
            left = True
        else:
            left = False
    return left,right

T = int(input())
for tc in range(1,T+1):
    ladder = [0]*100
    for i in range(100):
        ladder[i] = list(map(int,input().split()))

    #시작점 찾기
    minlen = 10000000
    idx = 0
    for j in range(100):
        if ladder[0][j] == 0: continue
        # 시작이 1. 시작할 수 있는 점부터 차례대로 출발
        print( "열 {} 출발합니다!".format(j))
        # 밑으로 내려가면서 높이가 99가 되면 끝나게
        h , w, count =  1, j, 1
        left, right = left_right(h,w,ladder)
        while h < 99 :
            print("#{} -  현재 h:{}행 w:{}열까지의 거리는 :{}".format(j, h, w, count))

            #오른쪽으로 가기
            if right == True and left == False :
                right = left = True
                while right == left == True :
                    # print("오른쪽으로 이동했습니다.")
                    count += 1
                    w += 1
                    left, right = left_right(h, w, ladder)
                    print("#{} -  현재 h:{}행 w:{}열까지의 거리는 :{}".format(j, h, w, count))
                if right == False and left == True: right = left = False


            if left == True and right == False :
                right = left = True
                while right == left == True :
                    # print("왼쪽으로 이동했습니다.")
                    count += 1
                    w-= 1
                    left, right = left_right(h, w, ladder)
                    print("#{} -  현재 h:{}행 w:{}열까지의 거리는 :{}".format(j, h, w, count))
                if right == True and left == False: right = left = False


            if right == left == False :
                # print("아래로 이동했습니다.")
                count+=1
                h+=1
                print("#{} -  현재 h:{}행 w:{}열까지의 거리는 :{}".format(j, h, w, count))
            left, right = left_right(h, w, ladder)

        if minlen > count :
            # print("원래 minlen:{} 였는데 {}으로 바뀌었습니다. 출발점 : {}".format(minlen,count, j))
            minlen = count
            idx = j
        print("현재 최소 길이는 : {}, 출발점은 :{} 최소길이를 가지는 출발점은 :{} 입니다. ".format(count,j, idx))
    print("#{} {}".format(tc, idx))





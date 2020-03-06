import sys

sys.stdin = open("Ladder2.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    ladder = [0] * 100
    for i in range(100):
        ladder[i] = list(map(int, input().split()))

    # 시작점 찾기
    minlen = 10000000
    idx = 0
    for j in range(100):
        if ladder[0][j] == 0: continue
        # 시작이 1. 시작할 수 있는 점부터 차례대로 출발
        # print("열 {} 출발합니다!".format(j))
        # 밑으로 내려가면서 높이가 99가 되면 끝나게
        h, w, count = 1, j, 1
        right = left = False
        while h < 99:
            # print("#{} -  현재 h:{}행 w:{}열까지의 거리는 :{}".format(j, h, w, count))
            # print("right:{} left:{}".format(right, left))
            # w == 0일 때
            if w == 0: left = False;
            if w == 99: right = False;

            # 오른쪽부터 살피기

            if ladder[h][w + 1] == 1 and w + 1 < 100:
                if left == False: right = True
                if left == False and right == True:
                    # print("오른쪽으로 이동했습니다.")
                    count += 1
                    w += 1
                    continue

            # 그다음 왼쪽
            if ladder[h][w - 1] == 1 and w - 1 > 0:
                if right == False: left = True
                # if left == right: left = True; right = False
                if left == True and right == False:
                    # print("왼쪽으로 이동했습니다.")
                    count += 1
                    w -= 1
                    continue

            right = left = False
            # 마지막으로 아래로
            if left == right and ladder[h + 1][w] == 1:
                # print("아래로 이동했습니다.")
                count += 1
                h += 1
                continue

        # print(" {}출발점의 도착까지의 길이는 {}이며 최종 도착지는 {}이고 지금 높이는 {}입니다. ".format(j, count, w, h))

        if minlen > count:
            # print("원래 minlen:{} 였는데 {}으로 바뀌었습니다. 출발점 : {}".format(minlen, count, j))
            minlen = count
            idx = j

        # print("현재 최소 길이는 : {}, 출발점은 :{} 최소길이를 가지는 출발점은 :{} 입니다. ".format(count, j, idx))
    print("#{} {}".format(tc, idx))





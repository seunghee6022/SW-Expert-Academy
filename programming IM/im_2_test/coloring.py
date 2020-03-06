import sys
#import numpy
sys.stdin = open("coloring.txt", "r")

T = int(input())
#N개의 색칠 영역 정보
for i in range(T):
    count = 0
    #색칠 정보가 들어있는 정보 리스트
    canvus = [0] * 10
    for a in range(10):
        canvus[a] = [0] * 10

    N = int(input())
    #캔버스에 색칠하기
    for j in range(N):
        r = list(map(int,input().split()))
        for row in range(r[0],r[2]+1):
            for column in range(r[1],r[3]+1):
                canvus[row][column]+=r[4]

    for elem in canvus :
        for e in elem :
            if e >= 3 :
                #print("e : {}".format(e))
                count+=1

    print("#{} {}".format(i+1,count))
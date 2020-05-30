import sys
sys.stdin= open("t.txt")

TC = int(input())
for tc in range(1, TC+1):
    data = [list(map(int, input().split())) for _ in range(9)]
    A =[0]*10
    flag = True
    #하나씩 해야하나다 해야하나 보다... 합으로 27 할랬는데 안되는듯.
    for i in range(9):
        for j in range(9):
            A[data[i][j]] = 1
        if sum(A) != 9:
            flag = False
            break
        A = [0] * 10


    if flag :
        for i in range(9):
            for j in range(9):
                A[data[j][i]] = 1
            if sum(A) != 9:
                flag = False
                break
            A = [0] * 10


    if flag:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                A = [0] * 10

                for i0 in range(3):
                    for j0 in range(3):
                        A[data[i+i0][j+j0]] = 1
                if sum(A) != 9:
                    flag = False
                    break
            if not flag : break

    if flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
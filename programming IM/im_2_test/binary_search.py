import sys
sys.stdin = open("binary_search.txt", 'r')

T= int(input())
for i in range(T):
    p, pa ,pb = map(int,input().split())
    counta, countb = 1, 1
    l = 1
    r = p
    searching = (r+l-1)/2

    #A부터 찾기
    # print("--------------------------count A--------------------------")
    while searching != pa:
        counta += 1

        if pa < searching :
            r = searching
        elif pa >searching :
            l = searching

        searching = int((r+l)/2)

    l = 1
    r = p
    searching = (r+l-1)/2
    # print("--------------------------count B--------------------------")
    while searching!= pb:
        countb += 1

        if pb < searching:
            r = searching
        elif pb > searching:
            l = searching

        searching = int((r + l) / 2)

    if counta == countb :
        result = '0'
    elif  counta > countb :
        result = 'B'
    else : result = 'A'


    print("#{} {}".format(i+1,result))


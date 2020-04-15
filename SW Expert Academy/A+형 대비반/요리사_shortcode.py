from itertools import combinations

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    sub_N=N//2
    arr=[list(map(int,input().split())) for _ in range(N)]
    row=[sum(i) for i in arr]
    col=[sum(i) for i in zip(*arr)]

    new_arr=[i+j for i,j in zip(row,col)] ### 같은 인덱스를 가지는 행과열을 더해주는 것

    allstat=sum(new_arr)//2       ### 전체 행렬값을 구해주는 것
    allstat -= new_arr[-1]        ### 1,2 vs 3,4 이나 3,4 vs 1,2은 동일한 결과를 나타내므로,
    mins=99999999                 ### 1재료를 미리 한팀으로 고정으로 정해줘서,
                                  ### 연산량을 줄여주기 위한 것.
                                  ### a b c d
                                  ### e f g h
                                  ### i j k l
                                  ### m n o p 가 있으면
                                  ### allstat은 a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p 이고,
                                  ### 1,2재료을 선택하고 new_arr 0,1를 뽑는다고 치면
                                  ### new_arr[0]=2a+b+c+d+e+i+m
                                  ### new_arr[1]=b+2f+j+n+e+g+h
                                  ### 두 개를 더 해주면
                                  ### 2a+2b+2e+2f+c+d+g+h+i+j+m+n이 되고 allstat에서 빼주면
                                  ###  (k+l+o+p)-(a+b+e+f) 이 되어 결과적으로,
                                  ### 3,4재료를 선택한 것에서 1,2재료를 선택한것을 빼준것과
                                  ### 동일 효과가 된다.



    for l in combinations(new_arr[:-1],sub_N-1):
        mins=min(mins,abs(allstat-sum(l)))

        if not mins:
            break
    print('#{} {}'.format(tc,mins))
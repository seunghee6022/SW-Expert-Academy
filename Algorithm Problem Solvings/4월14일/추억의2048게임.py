import sys
sys.stdin = open('t.txt','r')

def printarr(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

def changeDir(arr,direction):
    New = [[0]*N for _ in range(N)]
    if direction == 'left':
        for i in range(N):
            for j in range(N):
                New[i][j] = arr[i][-j-1] 
    
    elif direction == 'down':
        for i in range(N):
            for j in range(N):
                New[i][j] = arr[j][-i-1] 
        
    elif direction == 'up':
        for i in range(N):
            for j in range(N):
                New[i][j] = arr[-j-1][i]
    else :
        return arr

    return New

def calRight(arr):
    for j in range(N-1,0,-1):
        for i in range(N):
            #계산할 때 같은 숫자가 나오면 왼쪽에 더한값을 두어 다음에 계산못하게 함
            if arr[i][j] == arr[i][j-1]:
                arr[i][j-1] = 0
                arr[i][j] = arr[i][j]*2
            # 오른쪽이 0이면 왼쪽 숫자를 오른쪽으로 밀어 다음에 계산에 반영되게 함
            elif arr[i][j-1] == 0 :
                if arr[i][j] : 
                    arr[i][j-1], arr[i][j] = arr[i][j], arr[i][j-1]
  

    new = [[0]*N for _ in range(N)]
    # 계산이 다 끝나면 빈 공간은 왼쪽으로 밀기
    
    for i in range(N):
        loc = -1
        for j in range(N-1,-1,-1):
            if arr[i][j] : 
                new[i][loc] = arr[i][j]
                loc-=1
     
    return new

T = int(input())
for tc in range(1,T+1):
    N , direction = map(str, input().split())
    N = int(N)
    G = [[int(x) for x in input().split()] for _ in range(N)]
    
    new = changeDir(G,direction)
    arr = calRight(new)

    if direction == 'left':
        result = changeDir(arr,'left')
    elif direction == 'down':
        result = changeDir(arr,'up')
    elif direction == 'up':
        result = changeDir(arr,'down')
    else:
        result = arr
   
    print("#{}".format(tc))
    printarr(result)
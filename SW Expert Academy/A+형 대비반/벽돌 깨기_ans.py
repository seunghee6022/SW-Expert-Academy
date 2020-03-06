def shoot():





def remove




def npr(n,k,W,H):
    global minV

    if n==k :
        #구슬을 발사. 남은 벽돌 수 리턴
        r = shoot(k,W,H)
        if minV > r : minV = r

    else :
        for i in range(W): # 중복 순열
            p[n] = i
            npr(n+1,k,W,H)
            if minV ==0:
                return



T = int(input())
for tc in range(1,T+1):
    N, W, H = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(H)]

    # 벽돌 쏠 위치
    p = [0]* N
    minV = 10000000000000
    npr(0,N,W,H)

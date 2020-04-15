data = [7,4,2,0,0,6,0,7,9]
N = len(data)
Max = 0

for i in range(N-1):
    h = N - i - 1
    #가지치기
    if Max >= h : break
    for j in range(i+1,N):
        if data[i]<=data[j]:
            h-=1
    # Max = max(Max, h)
    if Max < h : Max = h

print(Max)



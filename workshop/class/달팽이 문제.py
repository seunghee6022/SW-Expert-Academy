nums = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
for i in range(5):
    print(nums[i])

#전체적인 회전 방향
dx_j = [1,0,-1,0]
dy_i =[0,1,0,-1]
#전체 회전방향 테두리 길이 카운트 하기
N = 5
edge = 1
xx = yy = count= elem= 0
while elem < 26:
    elem+=1
    nums[xx][yy] = elem
    count+=1
    for mode in range(4):
        if mode < 3 :
            for _ in range(N-edge):
                elem+=1
                yy += dx_j[mode]
                xx += dy_i[mode]
                print(xx,yy)
                nums[xx][yy] = elem
                print(nums[xx][yy])
        if mode == 3:
            for _ in range(N-edge-1):
                elem += 1
                yy += dx_j[mode]
                xx += dy_i[mode]
                print(xx, yy)
                nums[xx][yy] = elem
                print(nums[xx][yy])
    edge+=2
    xx = yy = count

for i in range(5):
    print(nums[i])

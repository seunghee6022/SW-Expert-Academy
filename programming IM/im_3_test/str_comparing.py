import sys
sys.stdin = open("str_comparing.txt", "r")

T = int(input())
for i in range(T):
    f = input()
    search_line = input()

    count = 0
    start_idx = -1
    while True :
        idx = search_line.find(f,start_idx+1,len(search_line))
        if idx == -1 :
            break
        else :
            start_idx = idx
            count+=1

    print("#{} {}".format(i+1,count))


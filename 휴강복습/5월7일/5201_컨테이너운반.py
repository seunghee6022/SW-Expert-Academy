import sys
sys.stdin = open('컨테이너운반_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    container = list(map(int, input().split()))
    container.sort()
    truck = list(map(int, input().split()))
    truck.sort()
    print(N, M, container, truck)
    # if truck[-1] < container[0] :
    #     print("#{} {}".format(tc,0))
    total = 0
    while truck and container:
        if container[0] > truck[-1]: break
        while container[-1] > truck[-1] and container:
            con = container.pop()
            print("pop", con)

        total += container[-1]
        t = truck.pop()
        c = container.pop()
        print(t,"->",c, container)

    print("#{} {}".format(tc,total))



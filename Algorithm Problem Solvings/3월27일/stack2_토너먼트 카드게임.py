import sys
sys.stdin = open('t.txt','r')

def rcp(i,j):
    if i==j : return i
    else :
        if card[i]==card[j] : return i
        elif card[i] == 1 :
            if card[j] == 2: return j
            else : return i
        elif card[i] == 2:
            if card[j] == 1 : return i
            else: return j
        elif card[i] == 3:
            if card[j] == 1 : return j
            else : return i

def winner(i,j):
    mid = (i+j)//2
    if j-i<=1 : return rcp(i,j)
    return rcp(winner(i,mid),winner(mid+1,j))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = [int(x) for x in input().split()]
    result = winner(0,N-1)

    print("#{} {}".format(tc,result))